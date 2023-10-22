"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Jan Kupeček

email: honzakupecek@gmail.com

discord: ming0092
"""

import requests
import bs4
import sys
import csv

def get_html(link):
    response = requests.get(link)
    html = bs4.BeautifulSoup(response.text, "html.parser")
    print("Downloading data:", link)
    return html

if len(sys.argv) != 3:
    print('Wrong number of arguments')
    quit()

html_content = get_html(sys.argv[1])

def get_towns() -> list:
    return [town.text for town in html_content.find_all("td", class_="overflow_name")]

def get_links() -> list:
    return [f"https://volby.cz/pls/ps2017nss/{link.a['href']}" for link in html_content.find_all("td", class_="cislo")]

def get_id() -> list:
    return [id.text for id in html_content.find_all("td", class_="cislo")]

def collect_parties() -> list:
    town_links = get_links()
    html_villages = get_html(town_links[0])
    return [party.text for party in html_villages.find_all("td", class_="overflow_name")]

def get_voter_stats() -> tuple:
    voters, attendance, valid_votes = [], [], []
    town_links = get_links()
    for link in town_links:
        html_path = get_html(link)
        voter = [v.text.replace('\xa0', ' ') for v in html_path.find_all("td", headers="sa2")]
        attend = [a.text.replace('\xa0', ' ') for a in html_path.find_all("td", headers="sa3")]
        valid = [c.text.replace('\xa0', ' ') for c in html_path.find_all("td", headers="sa6")]
        voters.extend(voter)
        attendance.extend(attend)
        valid_votes.extend(valid)
    return voters, attendance, valid_votes

def collect_votes() -> list:
    return [[v.text.strip() + ' %' for v in html.find_all("td", class_="cislo", headers=["t1sb4", "t2sb4"])] for html in map(get_html, get_links())]

def create_rows() -> list:
    voters, attendance, valid_ones = get_voter_stats()
    towns, ids, votes = get_towns(), get_id(), collect_votes()
    return [[i, t, v, a, vo] + vs for i, t, v, a, vo, vs in zip(ids, towns, voters, attendance, valid_ones, votes)]

def save_to_csv(url, output_file) -> None:
    try:
        header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
        content = create_rows()
        parties = collect_parties()
        print("Saving data to:", output_file)
        header.extend(parties)
        with open(output_file, 'w', newline='') as f:
            f_writer = csv.writer(f)
            f_writer.writerow(header)
            f_writer.writerows(content)
        print("Shutting down:", sys.argv[0])
    except IndexError:
        print("Error! Check URL.")
        quit()

if __name__ == '__main__':
    input_url = sys.argv[1]
    output_file_name = sys.argv[2]
    save_to_csv(input_url, output_file_name)
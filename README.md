# Elections scraper

Projekt 3 pro Engeto Python Akademii



# Popis projektu

Projekt slouží k vyscrapování volebních výsledků z parlamentních voleb 2017
Odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ



# Instalace knihoven

Knihovny a jejich verze, potřebné k instalaci, jsou v souboru requirements.txt

> pip install -r requirements.txt       # takto nainstalujete potřebné knihovny z přiloženého souboru



# Spuštění projektu

Projekt Elections_scraper.py spustíte v rámci příkazového řádku a musíte zadat dva povinné argumenty.

python Elections_scraper.py <odkaz_uzemniho_celku> <vysledny_soubor.csv>

Následně se Vám stáhnou vyscrapované výsledky voleb do souboru .csv


# Ukázka projektu

Výsledky hlasování pro okres Benešov:

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101
2. argument: Elections_results.csv


Spuštění programu:

python Elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "Elections_results.csv"


Průběh stahování:

Downloading data: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=529303&xvyber=2101
Saving data to: Elections_results.csv
Shutting down: Elections_scraper.py


Částečný výstup:

Kód obce, Název obce, Voliči v seznamu, Vydané obálky, Platné hlasy, Občanská demokratická strana, ...
529303, Benešov, 13 104, 8 485, 8 437, 12,46, ...
532568, Bernartice, 191, 148, 148, 2,70, ...
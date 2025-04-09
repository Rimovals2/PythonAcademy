"""
# Třetí projekt(3) do Engeto Online Python Akademie
# Projekt: Elections Scraper
# author: Slavomír Strnad
# email: Rimovals.s@seznam.cz
"""
import sys

# Kontrola nutných balíčků
try:
    import csv
    import os
    import argparse
    import requests
    from bs4 import BeautifulSoup
    from typing import List, Tuple
except ImportError as e:
    missing_pkg = str(e).split()[-1]
    print(f"Chyba: chybí balíček {missing_pkg}.")
    print("Ujistěte se, že máte nainstalovány všechny závislosti uvedené v requirements.txt.")
    print("Nainstalujete je například příkazem:")
    print("pip install -r requirements.txt")
    sys.exit(1)

# Stáhne obsah z URL, Při chybě ukončí program
def download_html(url: str) -> BeautifulSoup:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as err:
        print(f"Chyba při stahování {url}: {err}")
        sys.exit(1)
    return BeautifulSoup(response.text, "html.parser")

# Vrací seznam názvů obcí nalezených na stránce
def extract_cities(soup: BeautifulSoup) -> List[str]:
    return [cell.text.strip() for cell in soup.find_all("td", class_="overflow_name")]

# Vyhledá odkazy a vrátí seznam
def extract_links(soup: BeautifulSoup) -> List[str]:
    base_url = "https://volby.cz/pls/ps2017nss/"
    links = []
    for td in soup.find_all("td", class_="cislo"):
        a_tag = td.find("a")
        if a_tag and a_tag.has_attr("href"):
            links.append(base_url + a_tag["href"])
    return links

# Vrací seznam identifikačních čísel obcí
def extract_ids(soup: BeautifulSoup) -> List[str]:
    return [cell.text.strip() for cell in soup.find_all("td", class_="cislo")]

# Z detailu první obce získá názvy kandidujících stran.
def fetch_parties(first_detail_url: str) -> List[str]:
    soup = download_html(first_detail_url)
    return [cell.text.strip() for cell in soup.find_all("td", class_="overflow_name")]

# Ze zadané URL získá procentuální výsledky hlasování a statistiky
def fetch_votes_and_stats(detail_url: str) -> Tuple[List[str], str, str, str]:
    soup = download_html(detail_url)

    # Získání procentuálních výsledků hlasů.
    vote_cells = soup.find_all("td", class_="cislo", headers=["t1sb4", "t2sb4"])
    votes = [cell.text.strip() + ' %' for cell in vote_cells]

    # Statistické údaje.
    registered = soup.find("td", headers="sa2")
    envelopes  = soup.find("td", headers="sa3")
    valid_votes = soup.find("td", headers="sa6")

    reg_text = registered.text.strip() if registered else ""
    env_text = envelopes.text.strip() if envelopes else ""
    valid_text = valid_votes.text.strip() if valid_votes else ""

    return votes, reg_text, env_text, valid_text

#  Sestaví řádky pro CSV soubor
def build_csv_rows(soup: BeautifulSoup) -> List[List[str]]:
    rows = []
    cities = extract_cities(soup)
    ids = extract_ids(soup)
    detail_links = extract_links(soup)

    stats_registered = []
    stats_envelopes = []
    stats_valid = []
    all_votes = []

    total = len(detail_links)
    for idx, link in enumerate(detail_links, start=1):
        votes, registered, envelopes, valid_votes = fetch_votes_and_stats(link)
        stats_registered.append(registered)
        stats_envelopes.append(envelopes)
        stats_valid.append(valid_votes)
        all_votes.append(votes)

        progress = int((idx / total) * 100)
        remaining = total - idx
        # Aktualizace výpisu na jednom řádku
        sys.stdout.write(f"\rStahuji data: {progress}% dokončeno, zbývá {remaining} obcí")
        sys.stdout.flush()

    print()  # Přechod na nový řádek po dokončení.
    for i in range(len(cities)):
        row = [ids[i], cities[i], stats_registered[i], stats_envelopes[i], stats_valid[i]] + all_votes[i]
        rows.append(row)

    return rows

# Uloží zpracovaná data do CSV, kontrola zda není soubour použítý a vypíše cestu
def save_csv(filename: str, header: List[str], rows: List[List[str]]) -> None:
    try:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(header)
            writer.writerows(rows)
    except PermissionError:
        print(f"\nChyba: Soubor {filename} je momentálně otevřený nebo uzamčen. Zavřete soubor a zkuste to znovu.")
        sys.exit(1)

    abs_path = os.path.abspath(filename)
    print(f"\nData byla úspěšně uložena do souboru: {abs_path}")


def main():
    parser = argparse.ArgumentParser(description="Stahuje volební data a ukládá je do CSV souboru.")
    parser.add_argument("url", help="URL se základními informacemi o obcích.")
    parser.add_argument("output", help="Název výstupního CSV souboru.")
    args = parser.parse_args()

    base_soup = download_html(args.url)
    detail_links = extract_links(base_soup)
    if not detail_links:
        print("Nebyl nalezen žádný detailní odkaz na obce. Zkontrolujte zadanou URL adresu.")
        sys.exit(1)

    # Sestavení hlavičky CSV.
    header = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']
    parties = fetch_parties(detail_links[0])
    header.extend(parties)

    # Sestavení řádků pro CSV.
    rows = build_csv_rows(base_soup)

    # Uložení dat do CSV.
    save_csv(args.output, header, rows)
    print("Program byl úspěšně ukončen.")

if __name__ == '__main__':
    main()
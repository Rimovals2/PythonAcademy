# Scraper volebních výsledků 

Tento projekt je určen pro scrapování volebních výsledků z webu [volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). 
Skript **main.py** načte data z hlavní stránky, zpracuje tabulku, a nakonec uloží získaná data do CSV souboru. 
Data obsahují informace o obcích, počtech registrovaných voličů, vydaných obálkách, platných hlasů a hlasování pro jednotlivé kandidující strany.

1. **Přejdi do složky s projektem**:
   ```bash
   cd cesta/k/projektu
   ```

2. **Nainstaluj potřebné balíčky**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Spusť skript**:
   ```bash
   python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv
   ```

**Průběh Stahování**:
  ```bash
  Stahuji data: 10% dokončeno, zbývá 10 obcí
  ```

  **Částečný příklad výstupu**:
  ```bash
   Data byla úspěšně uložena do souboru: C:\Users\???\Desktop\python-academy\Project\Project03\vysledky.csv
   Program byl úspěšně ukončen.

  ```


## Obsah projektu

- **main.py** – Hlavní skript, který obsahuje všechny funkce: ověření argumentů, načtení stránek, a zápis výsledků do CSV.
- **requirements.txt** – Seznam potřebných knihoven potřebných k běhu skriptu (`requests` a `beautifulsoup4`)
- **vysledky_prostejov.csv** – Soubor  který se vytvoří po úspěšném spuštění skriptu.


# Projekt Nexus: Analiza kratera Jezero i navigacija rovera
 
## Executive Summary
 
Projekt Nexus fokusiran je na analizu geoprostornih i geokemijskih podataka kratera Jezero na Marsu s ciljem razvoja automatiziranog navigacijskog sustava za istraživački rover.
 
Ulazni podaci uključuju telemetrijske zapise (lokacije, dubine, pH vrijednosti, koncentracije metana), dok je krajnji cilj generiranje preciznih navigacijskih naredbi koje omogućuju sigurnu i optimiziranu kretnju robota kroz teren.
 
---
 
## Struktura repozitorija
 
```bash
project-nexus/
│
├── data/        # Ulazni CSV podaci
│   ├── mars_lokacije.csv
│   └── mars_uzorci.csv
│
├── src/         # Python skripte
│   ├── data_processing.py
│   ├── analysis.py
│   └── uplink.py
│
├── assets/      # Grafovi i vizualizacije
│   ├── korelacija.png
│   ├── toplinska_mapa.png
│   └── satelitska_mapa.png
│
└── README.md    # Dokumentacija projekta
```
 
---
 
## Metodologija obrade podataka (Data Wrangling)
 
Podaci su obrađeni korištenjem Python biblioteka:
 
* `pandas`
* `numpy`
 
### Ključni koraci:
 
1. **Učitavanje podataka**
 
```python
import pandas as pd
 
lokacije = pd.read_csv("data/mars_lokacije.csv")
uzorci = pd.read_csv("data/mars_uzorci.csv")
```
 
2. **Spajanje skupova podataka**
 
```python
df = pd.merge(lokacije, uzorci, on="id_lokacije")
```
 
3. **Čišćenje podataka**
 
* uklanjanje ekstremnih vrijednosti
* filtriranje senzorskog šuma
 
```python
df = df[(df["temperatura"] > -80) & (df["temperatura"] < 20)]
df = df[(df["ph"] > 3) & (df["ph"] < 10)]
```
 
4. **Normalizacija i priprema za analizu**
 
---
 
## Geoprostorna analiza i vizualizacija
 
Analiza uključuje vizualnu interpretaciju ključnih parametara.
 
### Korelacija varijabli
 
![Korelacija](assets/graf_1_korelacija.png)
 
Analiza pokazuje povezanost između koncentracije metana i dubine uzoraka.
 
---
 
### Toplinska mapa terena
 
![Toplinska mapa](assets/graf_2_mapa_metana(4).png)
 
Vizualizira varijacije dubine i temperature, omogućujući identifikaciju sigurnih ruta.
 
---
 
### Satelitska mapa (GPS projekcija)
 
![Satelitska mapa](assets/graf_2_mapa_metana(2).png)
 
Korišten je koncept **extent mapiranja** za precizno pozicioniranje podataka na stvarne koordinate.
 
Ova metoda omogućuje:
 
* realističnu navigaciju
* precizno mapiranje terena
* optimizaciju putanje robota
 
 
## Komunikacijski protokol (JSON Uplink)
 
Navigacijske naredbe generiraju se u JSON formatu:
 
```json
{
  "commands": [
    {
      "action": "MOVE",
      "coordinates": {
        "lat": -18.4,
        "lon": 77.5
      },
      "speed": 1.2
    },
    {
      "action": "SCAN",
      "duration": 10
    }
  ]
}
```
### Automatizacija generiranja naredbi
 
Umjesto ručnog unosa koristi se petlja:
 
```python
commands = []
 
for _, row in df.iterrows():
    cmd = {
        "action": "MOV
E",
        "coordinates": {
            "lat": row["lat"],
            "lon": row["lon"]
        }
    }
    commands.append(cmd)
```
 
Prednosti:
 
* skalabilnost
* smanjenje grešaka
* fleksibilnost sustava
 
 
## Inženjerski dnevnik (Troubleshooting Log)
 
### Problem 1: Neuspješno spajanje podataka
 
* **Uzrok:** pogrešan separator u CSV datoteci
* **Rješenje:** definiranje separatora pri učitavanju
 
```python
pd.read_csv("file.csv", sep=";")
```

 
### Problem 2: Rušenje skripte zbog tipova podataka
 
* **Uzrok:** string vrijednosti u numeričkim stupcima
* **Rješenje:** konverzija tipova
 
```python
df["temperatura"] = df["temperatura"].astype(float)
```
 
 
### Problem 3: Odbijen API zahtjev
 
* **Uzrok:** nedostajući autentifikacijski header
* **Rješenje:** dodavanje zaglavlja
 
```python
headers = {"Authorization": "Bearer TOKEN"}
```
 
 
##  Pokretanje projekta
 
### 1. Kloniranje repozitorija
 
```bash
git clone https://github.com/username/project-nexus.git
cd project-nexus
```
 
 
### 3. Pokretanje analize
 
```bash
python src/analysis.py

 
## Tehnologije
 
* Python 3.x
* pandas
* numpy
* matplotlib
* seaborn

 
## Buduća poboljšanja
 
* integracija s real-time API sustavom
* napredna AI navigacija
* optimizacija rute pomoću strojnog učenja

 
## Autor
 
Projekt razvijen u sklopu inženjerskog programa **Projekt Nexus - Noel Bernobic**.
 
---
 
##  Licenca
 
Ovaj projekt je otvorenog koda i dostupan pod MIT licencom

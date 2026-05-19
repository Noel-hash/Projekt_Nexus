import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import json

import requests

df_lokacije = pd.read_csv("mars_lokacije.csv", sep=';', decimal=',')

df_uzorci = pd.read_csv("mars_uzorci.csv", sep=';', decimal=',')

df_spajanje = pd.merge(df_lokacije, df_uzorci, on='ID_Uzorka')

df_notemp = df_spajanje[df_spajanje['Temp_Tla_C'] != 150.0]

df_cisto = df_noteap[df_notemp['H2O_Postotak'].astype(str).str.len() < 6].copy()

df_cisto['H2O_Postotak'] = pd.to_numeric(df_cisto['H2O_Postotak'])

kandidati = df_cisto[(df_cisto['Metan_Senzor'] == 'Pozitivno') & (df_cisto['Organske_Molekule'] == 'Da')]

# Graf 1

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df_cisto, x='Temp_Tla_C', y='H2O_Postotak', hue='Metan_Senzor')

plt.title("Odnos temperature i vlage")

plt.savefig('graf_1.png')

# Graf 2

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='Dubina_Busenja_cm', palette='viridis')

plt.title("Mapa planirane dubine bušenja")

plt.savefig('graf_2.png')

# Graf 3

plt.figure(figsize=(10, 6))

sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT',

                hue='Metan_Senzor', palette={'Pozitivno': 'red', 'Negativno': 'blue'})

plt.title("Detekcija metana po lokacijama")

plt.savefig('graf_3.png')

# Graf 4
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_cisto, x='GPS_LONG', y='GPS_LAT', hue='H2O_Postotak')
plt.scatter(kandidati['GPS_LONG'], kandidati['GPS_LAT'],
            marker='*', s=250, color='red', label='Kandidati (Org. molekule + Metan)')
plt.legend()
plt.title("Lokacije idealnih kandidata za analizu")
plt.savefig('graf_4.png')
plt.close()

# Graf 5
plt.figure(figsize=(12, 8))

granice = [
    df_cisto['GPS_LONG'].min(), df_cisto['GPS_LONG'].max(),
    df_cisto['GPS_LAT'].min(), df_cisto['GPS_LAT'].max()
]

slika = plt.imread("jezero_crater_satellite_map.jpg")
plt.imshow(slika, extent=granice, aspect="auto", alpha=0.7)

sns.scatterplot(data=df_cisto, x="GPS_LONG", y="GPS_LAT", alpha=0.3, label="Uzorci")

plt.scatter(
    kandidati["GPS_LONG"],
    kandidati["GPS_LAT"],
    marker="*",
    s=250,
    color="red",
    label="Kandidati za bušenje"
)

plt.legend()
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Misijska karta - Jezero krater")

plt.savefig("misijska_karta_jezero.jpg", dpi=200)

plt.close()

nuovi = pd.DataFrame({
    "umidita": [20, 65, 30],
    "temp": [38, 22, 35],
    "ore_secco": [48, 5, 36]
})

predizioni = modello.predict(nuovi)

for i, row in nuovi.iterrows():
    esito = "IRRIGARE" if predizioni[i] == 1 else "NON IRRIGARE"
    print(f"Zona {i+1}: umidita={row['umidita']:.0f}%, temp={row['temp']:.0f}C, ore_secco={row['ore_secco']:.0f}h -> {esito}")
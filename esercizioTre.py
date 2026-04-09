etichette = ['Non irrigare', 'Irrigare']
colori = ['#2ecc71', '#e74c3c']
medie = df.groupby('irrigare')[['umidita', 'temp', 'ore_secco']].mean()
variabili = ['Umidita (%)', 'Temperatura (C)', 'Ore senza pioggia']

fig, ax = plt.subplots(figsize=(8, 4))
x = np.arange(len(variabili))
larghezza = 0.35

for i, (classe, colore, etich) in enumerate(zip([0, 1], colori, etichette)):
    valori = medie.loc[classe]
    barre = ax.bar(x + i * larghezza, valori, larghezza, label=etich, color=colore)
    for b, v in zip(barre, valori):
        ax.text(b.get_x() + b.get_width()/2, v + 0.5, f'{v:.0f}', ha='center')

ax.set_title('Confronto medie per irrigazione')
ax.set_xticks(x + larghezza / 2)
ax.set_xticklabels(variabili)
ax.legend()
plt.savefig('eco_monitor_grafico.png', dpi=120)
plt.show()
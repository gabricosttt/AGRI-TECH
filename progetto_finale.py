import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

np.random.seed(42)

import numpy as np
import pandas as pd

n = 200
umidita = np.random.uniform(10, 80, n)
temp = np.random.uniform(15, 42, n)
ore_secco = np.random.uniform(0, 72, n)

irrigare = ((umidita < 35) & (temp > 28) & (ore_secco > 24)).astype(int)

# Creazione del DataFrame
df = pd.DataFrame({'umidita': umidita, 'temp': temp, 'ore_secco': ore_secco, 'irrigare': irrigare})

# Stampe richieste
print(f"Numero di letture totali: {len(df)}")
print(f"Zone da irrigare (1) e non (0):\n{df['irrigare'].value_counts()}")
print(f"Prime 4 righe del DataFrame:\n{df.head(4)}")


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

X = df[['umidita', 'temp', 'ore_secco']]
y = df['irrigare']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modello = RandomForestClassifier(n_estimators=50, random_state=42)
modello.fit(X_train, y_train)
y_pred = modello.predict(X_test)

print(f"{accuracy_score(y_test, y_pred)*100:.1f}%")

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(5, 4))
im = ax.imshow(cm, cmap='Greens')

ax.set_xticks(range(len(etichette)))
ax.set_yticks(range(len(etichette)))
ax.set_xticklabels(etichette)
ax.set_yticklabels(etichette)
ax.set_xlabel('Predetto')
ax.set_ylabel('Reale')
ax.set_title('Matrice di Confusione - Eco Monitor')

thresh = cm.max() / 2
for i in range(2):
    for j in range(2):
        color_text = 'white' if cm[i, j] > thresh else 'black'
        ax.text(j, i, str(cm[i, j]), 
                ha='center', va='center', 
                fontsize=18, fontweight='bold', 
                color=color_text)
      
plt.savefig('eco_monitor_risultati.png', dpi=120, bbox_inches='tight')

plt.show()
print("Grafico salvato correttamente come eco_monitor_risultati.png")

nuovi = pd.DataFrame({
    "umidita": [20, 65, 30],
    "temp": [38, 22, 35],
    "ore_secco": [48, 5, 36]
})

predizioni = modello.predict(nuovi)

for i, row in nuovi.iterrows():
    esito = "IRRIGARE" if predizioni[i] == 1 else "NON IRRIGARE"
    print(f"Zona {i+1}: umidita={row['umidita']:.0f}%, temp={row['temp']:.0f}C, ore_secco={row['ore_secco']:.0f}h -> {esito}")
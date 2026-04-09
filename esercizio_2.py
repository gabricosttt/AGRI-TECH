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
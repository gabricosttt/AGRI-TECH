# 🌱 ECO-MONITOR — Scrivi il Codice

**Obiettivo:** rispondendo a tutte le domande nell'ordine, avrai scritto l'intero programma funzionante.
Ogni risposta corrisponde a una riga (o blocco) del progetto finale.

---

## PARTE 1 — Import e Setup

**Domanda 1**
Scrivi le quattro righe di import necessarie per caricare: numpy (come `np`), pandas (come `pd`), matplotlib.pyplot (come `plt`), e il classificatore Random Forest da scikit-learn.

> 💡 Il classificatore Random Forest si trova in `sklearn.ensemble`.

---

**Domanda 2**
Dopo gli import, scrivi la riga che imposta il seme casuale a `42` per rendere i risultati riproducibili.

> 💡 La funzione si chiama su `np.random`.

---

## PARTE 2 — Dataset

**Domanda 3**
Imposta `n = 200`. Poi genera tre array numpy con valori casuali uniformi:
- `umidita` tra 10 e 80
- `temp` tra 15 e 42
- `ore_secco` tra 0 e 72

Scrivi le quattro righe di codice.

> 💡 Usa `np.random.uniform(minimo, massimo, n)` per ciascuna variabile.

---

**Domanda 4**
Scrivi la riga che crea la variabile `irrigare` applicando questa regola:
vale `1` se `umidita < 35` E `temp > 28` E `ore_secco > 24`, altrimenti `0`.

> 💡 Combina le condizioni con `&` tra parentesi, poi converti il risultato booleano in intero.

---

**Domanda 5**
Crea un DataFrame `df` con le colonne `umidita`, `temp`, `ore_secco` e `irrigare`.
Poi stampa: il numero di letture totali, quante zone vanno irrigate e quante no, e le prime 4 righe.

> 💡 Usa `pd.DataFrame({...})`. Per stampare usa tre `print()` separati.

---

## PARTE 3 — Grafico EDA

**Domanda 6**
Definisci:
- `etichette = ['Non irrigare', 'Irrigare']`
- `colori = ['#2ecc71', '#e74c3c']`
- Calcola `medie` raggruppando `df` per colonna `irrigare` e calcolando la media di `umidita`, `temp`, `ore_secco`.
- Definisci `variabili = ['Umidita (%)', 'Temperatura (C)', 'Ore senza pioggia']`

Scrivi le quattro righe.

> 💡 Usa `df.groupby('irrigare')[...].mean()` per calcolare le medie per classe.

---

**Domanda 7**
Crea la figura con `plt.subplots(figsize=(8, 4))`. Poi definisci:
- `x = np.arange(len(variabili))`
- `larghezza = 0.35`

Scrivi le tre righe.

> 💡 `np.arange(n)` genera `[0, 1, 2, ...]` — serve per posizionare le barre.

---

**Domanda 8**
Scrivi il ciclo `for` che disegna le barre per ciascuna classe (0 = non irrigare, 1 = irrigare).
Per ogni barra aggiungi anche il testo con il valore sopra la barra.
Il ciclo itera su `zip([0, 1], colori, etichette)`.

> 💡 Usa `ax.bar(x + i * larghezza, valori, larghezza, label=etich, color=colore, ...)`.
> Per il testo usa `ax.text(b.get_x() + b.get_width()/2, v + 0.5, f'{v:.0f}', ha='center', ...)`.

---

**Domanda 9**
Completa il grafico EDA: imposta titolo, etichette dell'asse x, legenda. Poi salva come `eco_monitor_grafico.png` con `dpi=120` e mostra il grafico.

> 💡 Usa `ax.set_xticks(x + larghezza / 2)` per centrare le etichette tra le barre.

---

## PARTE 4 — Modello ML

**Domanda 10**
Definisci `X` con le colonne `umidita`, `temp`, `ore_secco` e `y` con la colonna `irrigare`.
Poi dividi in training e test con `test_size=0.2` e `random_state=42`.

> 💡 Usa `train_test_split(X, y, ...)` — è già importato in cima.

---

**Domanda 11**
Crea il modello `RandomForestClassifier(n_estimators=50, random_state=42)`.
Addestralo sui dati di training. Poi genera le predizioni sul test set e stampane l'accuratezza.

> 💡 Per addestrare usa `.fit(X_train, y_train)`, per predire `.predict(X_test)`.
> Per l'accuratezza: `accuracy_score(y_test, y_pred)*100` con formato `:.1f%`.

---

## PARTE 5 — Grafico Risultati

**Domanda 12**
Calcola la matrice di confusione con `confusion_matrix(y_test, y_pred)`.
Poi crea una figura `(5, 4)` e visualizza la matrice come immagine con colormap `'Greens'`.
Aggiungi etichette agli assi e titolo.

> 💡 Usa `ax.imshow(cm, cmap='Greens')`. Le etichette degli assi sono `etichette` (già definite).

---

**Domanda 13**
Scrivi il ciclo doppio `for i in range(2): for j in range(2):` che stampa il numero `cm[i, j]` al centro di ogni cella. Il testo è bianco se il valore supera la metà del massimo, nero altrimenti.

> 💡 Usa `ax.text(j, i, str(cm[i, j]), ha='center', va='center', fontsize=18, fontweight='bold', color='white' if ... else 'black')`.

---

**Domanda 14**
Salva il grafico come `eco_monitor_risultati.png` con `dpi=120` e `bbox_inches='tight'`. Poi mostralo e stampa il messaggio di conferma.

---

## PARTE 6 — Simulatore

**Domanda 15**
Crea un DataFrame `nuovi` con 3 zone di test:
- umidita: 20, 65, 30
- temp: 38, 22, 35
- ore_secco: 48, 5, 36

Poi usa il modello per predire e stampa per ogni zona l'esito (`IRRIGARE` o `NON IRRIGARE`) con i valori dei sensori.

> 💡 Usa `modello.predict(nuovi)` e itera con `for i, row in nuovi.iterrows():`.
> La stringa di output: `f"  Zona {i+1}: umidita={row['umidita']:.0f}% ..."`.

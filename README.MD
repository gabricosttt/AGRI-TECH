# 🌱 Eco Monitor — Sistema di Irrigazione Intelligente

Modello di machine learning per prevedere se una zona agricola necessita di irrigazione, basandosi su dati ambientali simulati.

> 📚 Progetto realizzato nell'ambito del corso **RiSevet — Corso di Intelligenza Artificiale**

---

## 👥 Gruppo di Lavoro

| Nome | Cognome |
|---|---|
| Costanza | Gabriele |
| Gabriel | Caramanno |
| Sebastian | Di Bennardo |
| Liborio | Scozzari |
| Calogero | Crapanzano |

---

## 👥 Progetto & Team

**Progetto:** RiSeVet  
**Corso:** Intelligenza Artificiale

| Nome | Cognome |
|---|---|
| Costanza | Gabriele |
| Gabriel | Caramanno |
| Sebastian | Di Bennardo |
| Liborio | Scozzari |
| Calogero | Crapanzano |

---

## 📋 Descrizione

Eco Monitor analizza tre parametri ambientali — umidità del suolo, temperatura e ore trascorse senza pioggia — e addestra un classificatore Random Forest per decidere automaticamente se una zona va irrigata o meno.

---

## 🚀 Requisiti

Python 3.8+ e le seguenti librerie:

```
numpy
pandas
matplotlib
scikit-learn
```

Installazione rapida:

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## ▶️ Utilizzo

```bash
python eco_monitor.py
```

---

## ⚙️ Come funziona

### 1. Generazione del dataset
Vengono generate 200 letture casuali con i seguenti range:

| Variabile | Range |
|---|---|
| Umidità (%) | 10 – 80 |
| Temperatura (°C) | 15 – 42 |
| Ore senza pioggia | 0 – 72 |

La regola di etichettatura è:

> **Irrigare = 1** se `umidità < 35%` AND `temperatura > 28°C` AND `ore_secco > 24h`

### 2. Visualizzazione esplorativa
Viene generato un grafico a barre (`eco_monitor_grafico.png`) che confronta le medie delle tre variabili tra le classi *Irrigare* e *Non irrigare*.

### 3. Addestramento del modello
Il dataset viene suddiviso in training set (80%) e test set (20%). Viene addestrato un `RandomForestClassifier` con 50 alberi decisionali.

### 4. Valutazione
Vengono stampati l'accuratezza sul test set e una matrice di confusione (`eco_monitor_risultati.png`).

### 5. Predizione su nuovi dati
Il modello classifica 3 nuove zone di esempio:

| Zona | Umidità | Temperatura | Ore secco |
|---|---|---|---|
| 1 | 20% | 38°C | 48h |
| 2 | 65% | 22°C | 5h |
| 3 | 30% | 35°C | 36h |

---

## 📁 File generati

| File | Descrizione |
|---|---|
| `eco_monitor_grafico.png` | Grafico a barre delle medie per classe |
| `eco_monitor_risultati.png` | Matrice di confusione del modello |

---

## 🧠 Modello

- **Algoritmo:** Random Forest Classifier
- **Libreria:** scikit-learn
- **Parametri:** `n_estimators=50`, `random_state=42`
- **Split:** 80% train / 20% test
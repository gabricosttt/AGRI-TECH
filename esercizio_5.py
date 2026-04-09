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
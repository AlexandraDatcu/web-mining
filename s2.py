# Se da setul de date:
#
# http://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records
# https://www.kaggle.com/datasets/devvret/congressional-voting-records?resource=download
#
# Sa se clasifice printr-un arbore de decizie. Ce informatii suplimentarea capatam alegand  metoda respectiva?
# Ultimele 10% dintre randuri vor fi utilizate ca exemple de test.
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, classification_report
import matplotlib.pyplot as plt
# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("devvret/congressional-voting-records")
#
# print("Path to dataset files:", path)

df = pd.read_csv('house-votes-84.csv', header=None)
df.columns = ['party'] + [f'vote_{i}' for i in range(1,17)]
df = df.replace({'y': 1, 'n': 0, '?': -1})

# Separă features și etichete
X = df.drop('party', axis=1)
y = df['party']
# PAS 2: Înlocuim valorile categorice
df = df.replace({
    'y': 1,
    'n': 0,
    '?': -1  # semnal pentru necunoscut
})
y = df['party']
X = df.drop('party', axis=1)

# PAS 3: Împărțim datele (ultimele 10% pentru test)
test_size = int(0.1 * len(df))
X_train = X.iloc[:-test_size]
X_test = X.iloc[-test_size:]
y_train = y.iloc[:-test_size]
y_test = y.iloc[-test_size:]

# PAS 4: Antrenăm un arbore de decizie
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# PAS 5: Predicții și evaluare
y_pred = clf.predict(X_test)
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))

# PAS 6: Matrice de confuzie
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title("Confusion Matrix")
plt.show()

# PAS 7: Afișăm arborele
plt.figure(figsize=(20, 10))
plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True)
plt.title("Arbore de decizie: Congres")
plt.show()
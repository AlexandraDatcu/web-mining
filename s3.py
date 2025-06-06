# Se da setul de date: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing#. Sa se
# antreneze un mecanism care sa prezica daca un client va face un depozit pe termen
# lung. Ultimele 10% dintre randuri vor fi utilizate ca exemple de test.
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, confusion_matrix
import pandas as pd

df = pd.read_csv("bank-full.csv", sep=';')
print(df.head())

# PAS 3: Convertim coloanele categorice în numerice (one-hot encoding)
# Eliminăm coloana țintă 'y' temporar, o vom trata separat
X = pd.get_dummies(df.drop("y", axis=1))
print(X.head())
# PAS 4: Convertim etichetele 'yes' / 'no' în 1 / 0 pentru clasificare binară
y = df["y"].map({"yes": 1, "no": 0})

test_size = int(0.1 * len(df))
X_train = X.iloc[:-test_size]
X_test = X.iloc[-test_size:]
y_train = y.iloc[:-test_size]
y_test = y.iloc[-test_size:]

model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred, labels=[1, 0])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Deposit (yes)", "No deposit"])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

# TP (True Positives) = 434 → modelul a prezis "deposit (yes)" și a avut dreptate
#
# FN (False Negatives) = 1695 → a zis "no deposit", dar de fapt clientul a făcut depozit
#
# FP (False Positives) = 162 → a zis "deposit", dar clientul NU a făcut
#
# TN (True Negatives) = 2230 → a zis "no deposit" și a avut dreptate
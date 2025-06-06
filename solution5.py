### **Exercise 5: Applying a Classification Model**
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
# Exercise 5: Applying a Classification Model
# Objective: Train a simple classification model using the Titanic dataset.
#
# Steps:
# Use the preprocessed Titanic dataset from Exercise 4.
# Split the data into train and test sets (train_test_split).
# Train a Logistic Regression model to predict survival.
# Evaluate the model using accuracy, precision, and recall.
# Expected Output: A classification report showing model performance
# Step 1: Load the Titanic dataset
df = sns.load_dataset("titanic")

# Step 2: Feature Engineering (from Exercise 4)
df["family_size"] = df["sibsp"] + df["parch"] + 1  # Create new feature
df["age"].fillna(df["age"].median(), inplace=True)  # Handle missing age values
df["embarked"].fillna(df["embarked"].mode()[0], inplace=True)  # Handle missing embarked values
df.dropna(subset=["fare"], inplace=True)  # Remove rows with missing fare values
df = pd.get_dummies(df, columns=["sex", "embarked"], drop_first=True)  # One-hot encoding
print(df.columns)
#select futures and scale numerical columns
features = ["age", "fare", "family_size", "sex_male", "embarked_Q", "embarked_S"]
scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

X = df[features]
y = df["survived"]
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
train, test = train_test_split(df, test_size=0.2, random_state=42)
# Train a Logistic Regression model to predict survival.
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
# Step 7: Evaluate model performance
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
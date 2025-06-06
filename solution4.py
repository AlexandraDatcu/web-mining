### **Exercise 4: Feature Engineering for Classification**
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
# Exercise 4: Feature Engineering for Classification
# Objective: Create new features and scale them for machine learning.
#
# Steps:
# Load the Titanic dataset from Seaborn (sns.load_dataset('titanic')).
# Create a new feature: family_size = sibsp + parch + 1 (Total family members onboard).
# Encode categorical variables (sex, embarked) using one-hot encoding.
# Scale the numerical features (age, fare, family_size) using MinMaxScaler.
# Expected Output: A cleaned and transformed DataFrame ready for classification.
# Step 1: Load the Titanic dataset
df = sns.load_dataset("titanic")
df["family_size"] = df.parch + df.sibsp + 1
df["age"] = df["age"].fillna(df["age"].mean())
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
df["deck"] = df["deck"].fillna(df["deck"].mode()[0])

df = pd.get_dummies(data=df, columns=["sex","embarked"], drop_first=True)
# Scale the numerical features (age, fare, family_size) using MinMaxScaler.
scaler = MinMaxScaler()
df[["age", "fare", "family_size"]] = scaler.fit_transform(df[["age", "fare", "family_size"]])

print(df)


# train_model.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# =========================
# Load Dataset
# =========================

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target

print("\nDataset Shape:")
print(df.shape)

print("\nFeature Names:")
print(iris.feature_names)

print("\nClass Names:")
print(iris.target_names)

print("\nStatistical Summary:")
print(df.describe())

# =========================
# Visualizations
# =========================

sns.pairplot(df, hue="species")
plt.show()

df.hist(figsize=(10, 8))
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.show()

# =========================
# Split Data
# =========================

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# Models
# =========================

models = {
    "Logistic Regression":
        LogisticRegression(max_iter=200),

    "KNN":
        KNeighborsClassifier(n_neighbors=3),

    "Decision Tree":
        DecisionTreeClassifier(random_state=42)
}

best_model = None
best_accuracy = 0

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"\n{name}")
    print("Accuracy:", accuracy)

    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    print(
        classification_report(
            y_test,
            predictions
        )
    )

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# =========================
# Save Model
# =========================

joblib.dump(
    best_model,
    "model.pkl"
)

print("\nBest Model Saved!")
print("Accuracy:", best_accuracy)
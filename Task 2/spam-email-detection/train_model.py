import pandas as pd
import numpy as np
import string
import nltk
import joblib

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

nltk.download('stopwords')

# -----------------------------------
# Load Dataset
# -----------------------------------

df = pd.read_csv("dataset/spam.csv", encoding='latin-1')

df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print(df.head())

# -----------------------------------
# Preprocessing
# -----------------------------------

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    text = text.lower()

    text = ''.join(
        char for char in text
        if char not in string.punctuation
    )

    words = text.split()

    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

df['clean_text'] = df['message'].apply(preprocess_text)

# -----------------------------------
# Feature Extraction
# -----------------------------------

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df['clean_text'])

y = df['label'].map({
    'ham': 0,
    'spam': 1
})

# -----------------------------------
# Train Test Split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------------
# Models
# -----------------------------------

best_model = MultinomialNB()

best_model.fit(X_train, y_train)

predictions = best_model.predict(X_test)

print("Accuracy:",
      accuracy_score(y_test, predictions))

print("Precision:",
      precision_score(y_test, predictions))

print("Recall:",
      recall_score(y_test, predictions))

print("F1:",
      f1_score(y_test, predictions))

print("Confusion Matrix")

print(confusion_matrix(y_test, predictions))

# -----------------------------------
# Save Model
# -----------------------------------

joblib.dump(best_model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model Saved Successfully")
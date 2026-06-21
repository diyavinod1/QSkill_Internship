# 🤖 AI-Powered Spam Mail Detection System

> Because not every "Congratulations! You won an iPhone 🎉" message deserves your trust.

---

## 🚀 Project Overview

Welcome to my **AI-Powered Spam Mail Detection System**, built as **Task 2 of my AIML Internship at QSkill**.

This project uses **Natural Language Processing (NLP)** and **Machine Learning** to analyze text messages and classify them as:

✅ **Ham (Not Spam)**

🚨 **Spam**

The idea is simple:

A user enters a message, the AI analyzes the text, processes it using NLP techniques, converts it into numerical features using TF-IDF, and predicts whether the message is genuine or trying to scam you into clicking a suspicious link at 2 AM.

And yes... it can catch those classic:

> "URGENT! You have won ₹50,000. Claim now!"

messages 😭

---

## 🎯 Why I Built This

As part of my **AIML Internship at QSkill**, I wanted to build something that combines:

* Machine Learning
* NLP
* Model Training
* Web Development
* Real-time Predictions

instead of stopping at a Jupyter Notebook.

So I built a complete end-to-end project with:

✅ Data Processing

✅ NLP Pipeline

✅ Model Training

✅ Model Evaluation

✅ Flask Backend

✅ Modern Interactive Frontend

---

## 🧠 How It Works

### Step 1 — Text Preprocessing

The input message goes through an NLP pipeline:

* Convert text to lowercase
* Remove punctuation
* Remove special characters
* Remove stopwords
* Tokenization
* Stemming

Example:

Before:

```text
Congratulations! You won a free iPhone. Click here now.
```

After:

```text
congratul free iphon click
```

---

### Step 2 — Feature Extraction

The cleaned text is converted into numerical features using:

**TF-IDF Vectorization**

This helps the model understand which words are important and which are just noise.

---

### Step 3 — Machine Learning Prediction

The trained model analyzes the message and predicts:

```text
Spam
```

or

```text
Ham
```

along with a confidence score.

Example:

```text
🚨 Spam Message

Confidence: 98%
```

---

## 🛠️ Tech Stack

### Languages

* Python
* HTML
* CSS
* JavaScript

### Machine Learning

* Scikit-Learn

### NLP

* NLTK

### Backend

* Flask

### Data Handling

* Pandas
* NumPy

### Model Persistence

* Joblib

### Visualization

* Matplotlib
* Seaborn
* WordCloud

---

## 📂 Project Structure

```text
spam-mail-detector/
│
├── app.py
├── train_model.py
├── requirements.txt
├── spam_model.pkl
├── vectorizer.pkl
│
├── dataset/
│   └── spam.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── screenshots/
│
└── README.md
```

---

## 💡 Features

* Spam / Ham Classification
* NLP-Based Text Cleaning
* TF-IDF Feature Engineering
* Machine Learning Prediction
* Confidence Score Display
* Modern AI-Themed UI
* Glassmorphism Design
* Responsive Layout
* Real-Time Analysis

---

## 📊 Dataset

Dataset Used:

**SMS Spam Collection Dataset**

The dataset contains thousands of real SMS messages labeled as:

```text
spam
```

or

```text
ham
```

which were used to train and evaluate the model.

---

## 🧪 Model Training

The following models were experimented with:

* Multinomial Naive Bayes
* Logistic Regression
* Decision Tree Classifier

After evaluation using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

the best-performing model was selected and saved for deployment.

---

## 📈 Skills Gained

This project helped me learn and apply:

### Machine Learning

* Classification Problems
* Model Evaluation
* Performance Comparison

### NLP

* Text Cleaning
* Tokenization
* Stopword Removal
* Stemming
* TF-IDF Vectorization

### Development

* Flask Backend Development
* Frontend Integration
* API Communication
* Project Structuring

### Engineering Practices

* Model Serialization
* Modular Coding
* End-to-End ML Workflow

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <your-repo-link>
```

```bash
cd spam-mail-detector
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Train Model

```bash
python train_model.py
```

This generates:

```text
spam_model.pkl
vectorizer.pkl
```

---

### Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## 🎮 How To Use

1. Open the web application.
2. Enter any SMS or email-like message.
3. Click **Analyze Message**.
4. Let the AI do its thing.
5. Receive:

   * Prediction
   * Confidence Score

Example:

Input:

```text
Congratulations! You won a free iPhone. Click here now.
```

Output:

```text
🚨 Spam Message
Confidence: 98%
```

---

## 🎥 Demo Video

Want to see it in action?

Check out the demo video and project walkthrough on my LinkedIn post:

👉 **[Demo Video on LinkedIn](https://www.linkedin.com/posts/diyavinod1_ai-machinelearning-nlp-ugcPost-7474405431784849408-IrmI/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFgZTQ8BaC6JXgobyRLoVIbmid_nmnnksa0)**

---

## 🌱 Future Improvements

Some ideas I'm excited to explore:

* Deep Learning (LSTM)
* BERT-Based Spam Detection
* Explainable AI
* Spam Keyword Highlighting
* Prediction History
* Dark/Light Mode Toggle
* Email Integration
* Cloud Deployment

---

## 👩‍💻 Built By

**Diya Vinod**

3rd Year AIML Student

Building AI projects, solving DSA problems, and occasionally teaching machines how to ignore spam better than humans.

Currently exploring:

* Machine Learning
* NLP
* Generative AI
* Full-Stack AI Applications

---

## ⭐ Fun Fact

This project started as an internship task.

It ended with me training ML models, building APIs, designing a modern UI, debugging probability scores, fighting with Flask, arguing with Decision Trees, and somehow winning.

If you found this project interesting, consider giving the repository a ⭐.

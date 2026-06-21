# 🌸 AI-Powered Iris Flower Species Classification System

> Teaching a machine to identify flowers so I don't have to become a botanist. 😌🌷

A Machine Learning + Flask web application that predicts the species of an Iris flower based on its sepal and petal measurements.

Built as **Task 1 of the QSkill Internship Program**, this project takes the classic Iris dataset, trains multiple machine learning models, compares their performance, and deploys the best model through a modern web interface.

---

## 🚀 What Does This Project Do?

Give the system four flower measurements:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

And it will predict whether the flower is:

🌸 Iris Setosa

🌸 Iris Versicolor

🌸 Iris Virginica

along with a confidence score.

Because apparently flowers have personalities too. 🌚

---

## 🎯 Why I Built This

This project was created to understand the complete Machine Learning workflow from start to finish:

✅ Data Exploration

✅ Data Visualization

✅ Model Training

✅ Model Evaluation

✅ Model Deployment

✅ Flask Backend Development

✅ Frontend Integration

Instead of stopping after training a model in a notebook, I wanted to integrate it into a real web application that users can interact with.

---

## 💼 Internship Task

**QSkill Internship – Task 1**

Project Title:

**AI-Powered Iris Flower Species Classification System**

Task Objective:

Build an end-to-end machine learning application capable of classifying Iris flowers using the famous Iris dataset and deploy the model through a web-based interface.

---

## 🧠 Machine Learning Workflow

### Step 1: Dataset Loading

Loaded the Iris dataset using Scikit-Learn.

### Step 2: Exploratory Data Analysis

Performed:

* Dataset inspection
* Feature analysis
* Statistical summaries
* Class distribution analysis

### Step 3: Data Visualization

Generated:

* Scatter Plots
* Histograms
* Correlation Heatmaps

### Step 4: Model Training

Trained and compared:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree

### Step 5: Evaluation

Evaluated models using:

* Accuracy Score
* Confusion Matrix
* Classification Report

### Step 6: Application Integration

Saved the best-performing model using Joblib and integrated it with a Flask web application for real-time predictions.

---

## 🛠 Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* Pandas
* NumPy
* Joblib

### Data Visualization

* Matplotlib
* Seaborn

### Backend

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Development Tools

* VS Code
* Git
* GitHub

---

## ✨ Features

* Predicts Iris flower species instantly
* Confidence score for every prediction
* Multiple ML models compared
* Responsive UI
* Modern glassmorphism design
* Beginner-friendly code structure
* Real-world ML deployment workflow

---

## 📂 Project Structure

```bash
iris-flower-classifier/
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
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

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/iris-flower-classifier.git
```

### Move into the Project Folder

```bash
cd iris-flower-classifier
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

Run:

```bash
python train_model.py
```

This will:

* Load the dataset
* Train multiple models
* Compare performance
* Save the best model as:

```bash
model.pkl
```

---

## 🌐 Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Your flower-predicting AI is now running locally. 🚀

---

## 🎮 How to Use

1. Open the web application.

2. Enter:

   * Sepal Length
   * Sepal Width
   * Petal Length
   * Petal Width

3. Click:

```text
Predict Species
```

4. Receive:

✅ Predicted Flower Species

✅ Confidence Score

---

## 🎥 Demo Video

Want to see it in action?

📹 LinkedIn Demo:

[LinkedIn Demo Video]([PASTE_YOUR_LINKEDIN_POST_LINK](https://www.linkedin.com/posts/diyavinod1_ai-machinelearning-artificialintelligence-activity-7471223369426722816-wVfD?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFgZTQ8BaC6JXgobyRLoVIbmid_nmnnksa0))

Trust me, the flowers were classified respectfully. 🌸😂

---

## 📈 Sample Prediction

Input:

```text
Sepal Length : 5.1
Sepal Width  : 3.5
Petal Length : 1.4
Petal Width  : 0.2
```

Output:

```text
Predicted Species:
Iris Setosa

Confidence:
99%+
```

---

## 🧩 Skills Gained

Through this project I learned:

* Machine Learning Fundamentals
* Classification Algorithms
* Exploratory Data Analysis
* Data Visualization
* Model Evaluation Techniques
* Flask Development
* API Handling
* Frontend Development
* Model Deployment
* Git & GitHub Workflow
* End-to-End Project Development

Most importantly:

**How to turn a machine learning model into something an actual user can interact with.**

---

## 👩‍💻 Developed By

**Diya Vinod**

AI/ML Enthusiast • Full Stack Learner • Problem Solver

Currently building projects, solving DSA, exploring AI, and occasionally convincing flowers to reveal their species. 🌸🤖

If you found this project interesting, feel free to ⭐ the repository.

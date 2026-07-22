# ai-student-predictor
# 🎓 AI-Powered Student Performance Predictor

An end-to-end Machine Learning project that predicts a student's academic grade based on study habits, attendance, and classroom participation. The project includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.

---

## 📌 Project Overview

Educational institutions often struggle to identify students who may require additional academic support. This project uses Machine Learning to predict student grades based on academic and behavioral factors, helping educators make data-driven decisions.

---

## 🚀 Features

* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data Cleaning & Preprocessing
* 🤖 Machine Learning Model Training
* 📈 Model Performance Evaluation
* 🎯 Student Grade Prediction
* 🌐 Interactive Streamlit Web Application
* 💾 Model Serialization using Joblib

---

## 📂 Project Structure

```text
AI-Student-Performance-Predictor/
│
├── data/
│   └── student_performance.csv
│
├── notebooks/
│   └── Student_Performance_Predictor.ipynb
│
├── app.py
├── requirements.txt
├── student_model.pkl
├── scaler.pkl
├── label_encoder.pkl
├── README.md
└── .gitignore
```

---

## 📊 Dataset Features

| Feature                 | Description                     |
| ----------------------- | ------------------------------- |
| student_id              | Unique Student ID               |
| weekly_self_study_hours | Weekly self-study hours         |
| attendance_percentage   | Attendance percentage           |
| class_participation     | Class participation score       |
| total_score             | Total examination score         |
| grade                   | Target variable (Student Grade) |

> **Note:** During model training, `student_id` is excluded because it does not contribute to prediction. If the goal is to predict grades before exams, `total_score` should also be excluded to avoid data leakage.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Git & GitHub

---

## 📈 Machine Learning Workflow

```text
Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Train-Test Split
      │
      ▼
Feature Scaling
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Model
      │
      ▼
Streamlit Deployment
```

---

## 🤖 Machine Learning Models

The following models were trained and compared:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

The best-performing model was selected for deployment.

---

## 📊 Evaluation Metrics

The models were evaluated using:

* Accuracy
* Confusion Matrix
* Classification Report
* Precision
* Recall
* F1-Score

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/Vishhwassri32/ai-student-predictor.git
```

Move into the project directory:

```bash
cd ai-student-predictor
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 📷 Application Preview

*(Add screenshots after deployment.)*

---

## 📌 Future Improvements

* Student risk prediction (Low / Medium / High)
* Personalized study recommendations
* Attendance trend visualization
* Performance dashboard
* Database integration
* Cloud deployment
* Model explainability using SHAP

---

## 👨‍💻 Author

**Vishwas Srivastava** 
* 🎓 B.Tech CSE (Data Science)
* 💼 Aspiring Data Scientist & Machine Learning Engineer
## ⭐ Support
If you found this project helpful, consider giving it a ⭐ on GitHub. It helps others discover the project and motivates future improvements.
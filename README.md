# Customer Churn Prediction

## Project Overview

This project predicts whether a telecom customer is likely to leave the company (Churn) using Machine Learning.

The goal is to identify customers who may leave and help the company improve customer retention.

## Dataset

- Dataset: Telco Customer Churn
- Total Records: 7043
- Total Columns: 21
- Target Column: Churn
- Target Values: Yes / No

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Train-Test Split
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Comparison

## Model Performance

Two Machine Learning models were trained and compared.

| Model | Accuracy | F1 Score |
|---|---:|---:|
| Logistic Regression | 80.55% | 0.60 |
| Random Forest | 76.79% | 0.59 |

### Final Model

Logistic Regression was selected because it achieved better accuracy and F1 score.

## Project Structure

Customer_Churn_Prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── churn_eda.ipynb
│
└── README.md

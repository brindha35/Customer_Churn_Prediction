# Customer Churn Prediction – Project Report

## 1. Problem Statement
The objective of this project is to predict whether a telecom customer is likely to leave the service (churn) or continue using it.

## 2. Dataset
The project uses the Telco Customer Churn dataset. It contains customer details, service information, contract details, and billing information.

## 3. Method
- Performed data cleaning and exploratory data analysis.
- Prepared customer features for machine learning.
- Trained an XGBoost classification model using a preprocessing pipeline.
- Used the trained model to predict churn for new customers.
- Saved the model using Joblib.

## 4. Results
- ROC-AUC: 0.8227
- F1 Score: 0.5869
- Confusion Matrix:

```text
[[913, 122],
 [168, 206]]
```

The sample new customer prediction was No Churn, with a churn probability of 5.37%.

## 5. Limitations
- The model may not predict every customer correctly.
- The sample prediction uses only one customer record.
- Customer behaviour may change over time.

## 6. Recommendations
- Focus on customers with high predicted churn probability.
- Offer suitable retention plans and customer support.
- Monitor model performance with new customer data.
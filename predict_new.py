import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")

print("Model loaded successfully!")

new_customers = pd.read_csv("new_customers.csv")

print(new_customers.head())


predictions = model.predict(new_customers)
probabilities = model.predict_proba(new_customers)[:, 1]

results = new_customers.copy()
results["Churn_Prediction"] = predictions
results["Churn_Probability"] = probabilities

results.to_csv("predictions.csv", index=False)

print("Predictions saved successfully!")
print(results)
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/synthetic_dataset.csv")

df["Weather"] = df["Weather"].map({"Clear": 0, "Rain": 1, "Fog": 2})

X = df[["Previous_Delay_Min", "Peak_Hour", "Weather"]]
y = df["Delay_Minutes"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "models/delay_model.pkl")

print("Model trained and saved successfully!")
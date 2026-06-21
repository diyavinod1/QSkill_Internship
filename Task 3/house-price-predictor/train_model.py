import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("dataset/housing.csv")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

# =====================================
# DATA CLEANING
# =====================================

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values safely
for col in df.columns:

    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())

    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# =====================================
# ENCODE CATEGORICAL COLUMNS
# =====================================

categorical_cols = df.select_dtypes(
    include=["object", "string"]
).columns

df = pd.get_dummies(
    df,
    columns=categorical_cols,
    drop_first=True
)

print("\nColumns After Encoding:")
print(df.columns.tolist())

# =====================================
# FEATURES & TARGET
# =====================================

X = df.drop("price", axis=1)
y = df["price"]

print("\nFeature Count:", len(X.columns))

# =====================================
# FEATURE SCALING
# =====================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================
# MODELS
# =====================================

models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )
}

best_model = None
best_score = -999

print("\n====================================")
print("MODEL EVALUATION")
print("====================================")

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(mse)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print(f"\n{name}")
    print("-" * 40)
    print("MSE :", round(mse, 2))
    print("RMSE:", round(rmse, 2))
    print("MAE :", round(mae, 2))
    print("R²  :", round(r2, 4))

    if r2 > best_score:
        best_score = r2
        best_model = model

# =====================================
# SAVE MODEL
# =====================================

joblib.dump(
    best_model,
    "models/house_price_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

joblib.dump(
    X.columns.tolist(),
    "models/feature_names.pkl"
)

print("\n====================================")
print("MODEL SAVED SUCCESSFULLY")
print("====================================")

print("Best R² Score:", round(best_score, 4))

print("\nSaved Files:")
print("models/house_price_model.pkl")
print("models/scaler.pkl")
print("models/feature_names.pkl")
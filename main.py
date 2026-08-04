import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

import joblib


# -------------------------------
# Load Dataset
# -------------------------------

data = pd.read_csv("dataset/Dataset.csv")

print("Dataset Loaded Successfully!")
print(data.head())


# -------------------------------
# Handle Missing Values
# -------------------------------

processed_data = data.copy()

processed_data["Cuisines"] = processed_data["Cuisines"].fillna("Unknown")

print("\nMissing Values:")
print(processed_data.isnull().sum())


# -------------------------------
# Encode Categorical Variables
# -------------------------------

encoder = LabelEncoder()

categorical_columns = processed_data.select_dtypes(
    include="object"
).columns


print("\nCategorical Columns:")
print(categorical_columns)


for column in categorical_columns:
    processed_data[column] = encoder.fit_transform(
        processed_data[column]
    )


print("\nAfter Encoding:")
print(processed_data.head())


# -------------------------------
# Split Features and Target
# -------------------------------

X = processed_data.drop(
    "Aggregate rating",
    axis=1
)

y = processed_data["Aggregate rating"]


print("\nFeatures Shape:")
print(X.shape)

print("Target Shape:")
print(y.shape)



# -------------------------------
# Train Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print("\nTraining Data:")
print(X_train.shape)

print("Testing Data:")
print(X_test.shape)



# -------------------------------
# Train Model
# -------------------------------

model = DecisionTreeRegressor(
    random_state=42
)


model.fit(
    X_train,
    y_train
)


print("\nModel training completed!")



# -------------------------------
# Prediction
# -------------------------------

y_pred = model.predict(
    X_test
)


print("\nFirst 10 Predictions:")
print(y_pred[:10])



# -------------------------------
# Model Evaluation
# -------------------------------

mse = mean_squared_error(
    y_test,
    y_pred
)


r2 = r2_score(
    y_test,
    y_pred
)


print("\nMean Squared Error:")
print(mse)


print("\nR2 Score:")
print(r2)



# -------------------------------
# Feature Importance
# -------------------------------

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance": model.feature_importances_

})


importance = importance.sort_values(
    by="Importance",
    ascending=False
)


print("\nFeature Importance:")
print(importance)



# -------------------------------
# Create Feature Importance Graph
# -------------------------------

top_features = importance.head(10)


plt.figure(figsize=(10,6))


plt.barh(
    top_features["Feature"],
    top_features["Importance"]
)


plt.xlabel(
    "Importance Score"
)


plt.ylabel(
    "Features"
)


plt.title(
    "Top 10 Features Affecting Restaurant Ratings"
)


plt.gca().invert_yaxis()


plt.tight_layout()


# Save graph

plt.savefig(
    "feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)


print(
    "\nFeature importance graph saved successfully!"
)


plt.show()



# -------------------------------
# Save Model
# -------------------------------

joblib.dump(
    model,
    "restaurant_rating_model.pkl"
)


print(
    "\nModel saved successfully!"
)
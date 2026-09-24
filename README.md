# 🍽️ Restaurant Rating Prediction

## 📌 Project Overview

**Restaurant Rating Prediction** is a Machine Learning project that predicts restaurant **Aggregate Ratings** using restaurant-related features.

The project uses a **Decision Tree Regressor** to learn patterns from restaurant data and predict ratings. The workflow includes data loading, missing-value handling, categorical encoding, train-test splitting, model training, prediction, evaluation, and feature-importance analysis.

The project is implemented in Python using **Pandas, Matplotlib, Scikit-learn, and Joblib**.

---

## 🎯 Problem Statement

Restaurant ratings can be influenced by different factors such as location, cuisine, price range, online ordering, table booking, and customer votes.

The objective of this project is to build a Machine Learning regression model that learns from existing restaurant data and predicts the **Aggregate Rating** of restaurants.

---

## 🚀 Objectives

* Load and inspect the restaurant dataset
* Handle missing values
* Identify categorical features
* Convert categorical data into numerical values
* Separate input features and target variable
* Split the dataset into training and testing data
* Train a Decision Tree Regression model
* Predict restaurant ratings
* Evaluate the model using MSE and R² Score
* Analyze feature importance
* Generate a feature-importance visualization
* Save the trained Machine Learning model

---

## 📊 Dataset

The project uses a restaurant dataset containing information about restaurants and their ratings.

Some relevant attributes include:

* Restaurant Name
* Location
* Cuisines
* Restaurant Type
* Price Range
* Online Ordering
* Table Booking
* Votes
* Aggregate Rating

### Target Variable

**Aggregate Rating**

The `Aggregate rating` column is used as the target variable that the Machine Learning model attempts to predict.

The dataset used by the program is located at:

```text
dataset/Dataset.csv
```

---

## 🧹 Data Preprocessing

The following preprocessing steps are performed in `main.py`:

1. Load the dataset using Pandas.
2. Create a copy of the original dataset.
3. Handle missing values in the `Cuisines` column by replacing them with `"Unknown"`.
4. Identify categorical columns.
5. Encode categorical variables using `LabelEncoder`.
6. Separate the features (`X`) and target (`y`).
7. Split the data into training and testing sets.

The dataset is divided using:

```text
80% Training Data
20% Testing Data
```

A `random_state` of `42` is used to make the train-test split reproducible.

---

## 🤖 Machine Learning Model

### Decision Tree Regressor

This project uses the **Decision Tree Regressor** from Scikit-learn.

```python
DecisionTreeRegressor(random_state=42)
```

The model is trained using the training dataset and then used to predict restaurant ratings for the test dataset.

### Why Decision Tree Regression?

A Decision Tree Regressor can learn relationships between input features and a numerical target value. Since **Aggregate Rating** is a numerical value, regression is appropriate for this prediction task.

---

## 📈 Model Evaluation

The trained model is evaluated using two regression metrics.

### Mean Squared Error (MSE)

MSE measures the average squared difference between the actual ratings and the predicted ratings.

A lower MSE indicates smaller prediction errors.

### R² Score

R² Score measures how well the model explains the variation in the target variable.

The actual MSE and R² values are displayed when `main.py` is executed.

Example output:

```text
Mean Squared Error:
<value generated when the program runs>

R2 Score:
<value generated when the program runs>
```

The values are intentionally not hard-coded in this README because they depend on the actual execution of the model.

---

## 🔍 Feature Importance

The Decision Tree model provides feature-importance values that indicate the relative contribution of each feature to the model's predictions.

The program:

1. Calculates feature importance.
2. Sorts the features by importance.
3. Selects the top 10 features.
4. Creates a horizontal bar chart.
5. Saves the chart as:

```text
feature_importance.png
```

### Feature Importance Visualization

The generated visualization is included in this repository:

```text
feature_importance.png
```

This visualization helps identify which restaurant-related features had the greatest influence on the trained Decision Tree model.

---

## 📁 Project Structure

The current repository structure is:

```text
Predict-Restaurant-Ratings/
│
├── dataset/
│   └── Dataset.csv
│
├── .gitignore
├── README.md
├── feature_importance.png
├── main.py
└── requirements.txt
```

### File Description

| File / Folder            | Description                                                   |
| ------------------------ | ------------------------------------------------------------- |
| `dataset/`               | Contains the restaurant dataset                               |
| `Dataset.csv`            | Input dataset used by the Machine Learning program            |
| `main.py`                | Main Python program for training and evaluating the model     |
| `feature_importance.png` | Generated feature-importance visualization                    |
| `requirements.txt`       | Python libraries required to run the project                  |
| `.gitignore`             | Specifies files and folders that should not be tracked by Git |
| `README.md`              | Project documentation                                         |

---

## 🛠️ Technologies Used

| Technology   | Purpose                                   |
| ------------ | ----------------------------------------- |
| Python       | Programming language                      |
| Pandas       | Data loading and data processing          |
| Matplotlib   | Data visualization                        |
| Scikit-learn | Machine Learning and evaluation           |
| Joblib       | Saving the trained Machine Learning model |
| Git          | Version control                           |
| GitHub       | Source-code hosting                       |

---

## 📦 Required Libraries

The project uses the libraries listed in `requirements.txt`.

The main libraries used in the Python program are:

```text
pandas
numpy
matplotlib
scikit-learn
joblib
```

> Note: `numpy` is currently imported in the Python file but is not directly used in the calculations.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Padmavati2611/Predict-Restaurant-Ratings.git
```

### 2. Open the project folder

```bash
cd Predict-Restaurant-Ratings
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

Make sure the terminal is opened inside the project folder.

Run:

```bash
python main.py
```

If your system uses the Python launcher on Windows, you can also use:

```bash
py main.py
```

The program will:

1. Load the dataset.
2. Display the first few records.
3. Check missing values.
4. Encode categorical columns.
5. Split the data into training and testing sets.
6. Train the Decision Tree Regressor.
7. Generate predictions.
8. Calculate MSE.
9. Calculate R² Score.
10. Display feature importance.
11. Generate the feature-importance graph.
12. Save the trained model.

---

## 🔄 Project Workflow

```text
Restaurant Dataset
        ↓
Load Dataset
        ↓
Handle Missing Values
        ↓
Encode Categorical Variables
        ↓
Separate Features and Target
        ↓
Train-Test Split
        ↓
Decision Tree Regressor
        ↓
Model Training
        ↓
Prediction
        ↓
MSE + R² Evaluation
        ↓
Feature Importance Analysis
        ↓
Feature Importance Graph
        ↓
Save Trained Model
```

---

## 💾 Model Output

The Python program saves the trained Machine Learning model using Joblib.

The generated model file is:

```text
restaurant_rating_model.pkl
```

This file is created when the program is successfully executed.

The saved model can be used later for prediction without retraining the model, provided that the same preprocessing approach is applied to new input data.

---

## 📷 Project Result

The project generates a feature-importance visualization:

```text
feature_importance.png
```

The graph displays the top 10 features according to the Decision Tree model's calculated feature-importance values.

The numerical model results, including **MSE** and **R² Score**, are printed in the terminal when the program is executed.

---

## 💡 Key Outcomes

Through this project, the Machine Learning workflow for a regression problem was implemented from dataset loading to model evaluation.

The project demonstrates:

* Data preprocessing
* Missing-value handling
* Categorical encoding
* Train-test splitting
* Decision Tree Regression
* Prediction
* Regression evaluation
* Feature-importance analysis
* Data visualization
* Model serialization using Joblib

---

## 🎓 Learning Outcomes

This project helped develop practical experience with:

* Python programming
* Pandas data processing
* Machine Learning preprocessing
* Categorical data encoding
* Regression algorithms
* Decision Tree models
* Model evaluation
* Feature importance
* Matplotlib visualization
* Saving Machine Learning models
* Git and GitHub

---

## 🔮 Future Improvements

Possible improvements for the project include:

* Use a more robust preprocessing pipeline for categorical variables.
* Compare Decision Tree Regression with other regression algorithms.
* Perform hyperparameter tuning.
* Add additional evaluation metrics such as MAE and RMSE.
* Build an interactive prediction interface.
* Deploy the trained model as a web application.
* Improve feature engineering.
* Add prediction for new restaurant records.

---

## 👩‍💻 Author

**Padmavati B**

AI & ML Engineering Student

GitHub:
https://github.com/Padmavati2611

---

## 📌 Project Purpose

This project was developed for educational and practical Machine Learning learning purposes.

It demonstrates the complete basic workflow of building a regression model for predicting restaurant ratings using Python and Scikit-learn.

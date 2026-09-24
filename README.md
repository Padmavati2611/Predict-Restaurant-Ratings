# 🍽️ Restaurant Rating Prediction

## 📌 Project Overview

**Restaurant Rating Prediction** is a Machine Learning project that predicts the **aggregate rating of a restaurant** based on different restaurant-related features.

The project uses restaurant data to perform data preprocessing, exploratory data analysis, feature encoding, model training, and evaluation.

The main objective is to understand which restaurant features can be used to predict restaurant ratings using Machine Learning.

---

## 🎯 Problem Statement

Restaurant ratings are influenced by several factors such as restaurant location, cuisine, price range, online ordering, table booking, and customer votes.

The objective of this project is to build a Machine Learning model that can learn from existing restaurant data and predict the expected rating of a restaurant.

---

## 🚀 Objectives

* Clean and preprocess the restaurant dataset
* Handle missing values
* Perform Exploratory Data Analysis (EDA)
* Analyze relationships between restaurant features and ratings
* Encode categorical variables
* Split the dataset into training and testing sets
* Train Machine Learning regression models
* Evaluate model performance
* Identify important features affecting restaurant ratings
* Generate predictions for restaurant ratings

---

## 📊 Dataset

The project uses a restaurant dataset containing information such as:

* Restaurant Name
* Location
* Restaurant Type
* Cuisines
* Average Cost for Two
* Table Booking
* Online Ordering
* Votes
* Price Range
* Aggregate Rating

### Target Variable

**Aggregate Rating**

The target variable represents the restaurant's overall rating.

---

## 🧹 Data Preprocessing

The following preprocessing steps are performed:

1. Load the restaurant dataset using Pandas.
2. Inspect the dataset for missing values.
3. Handle missing values appropriately.
4. Remove unnecessary columns.
5. Convert categorical features into numerical representations.
6. Select relevant features for Machine Learning.
7. Separate input features and target variable.
8. Split the dataset into training and testing sets.

---

## 🔍 Exploratory Data Analysis

EDA is performed to understand the dataset and identify useful patterns.

The analysis includes:

* Rating distribution
* Restaurant distribution
* Price range analysis
* Votes vs. rating analysis
* Cuisine analysis
* Correlation analysis
* Feature importance analysis

Visualizations are created using Matplotlib and Seaborn where applicable.

---

## 🤖 Machine Learning

This project treats restaurant rating prediction as a **regression problem**.

### Models Used

Depending on the implementation, the project can use:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

The trained models are evaluated on the test dataset.

---

## 📈 Model Evaluation

The model performance can be evaluated using regression metrics such as:

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

These metrics help measure how accurately the model predicts restaurant ratings.

> **Note:** The exact metric values should be updated here after running the final model.

### Example

```text
Model: Random Forest Regressor

MAE  : [add result]
RMSE : [add result]
R²   : [add result]
```

---

## 💡 Key Insights

The analysis helps identify relationships between restaurant characteristics and ratings.

Some factors that can be investigated include:

* Number of customer votes
* Price range
* Restaurant type
* Cuisine
* Location
* Online ordering availability
* Table booking availability

The final insights should be updated according to the actual results obtained from the dataset.

---

## 🛠️ Technologies Used

| Technology                      | Purpose                   |
| ------------------------------- | ------------------------- |
| Python                          | Programming language      |
| Pandas                          | Data manipulation         |
| NumPy                           | Numerical operations      |
| Matplotlib                      | Data visualization        |
| Seaborn                         | Statistical visualization |
| Scikit-learn                    | Machine Learning          |
| Jupyter Notebook / Google Colab | Development environment   |
| Git & GitHub                    | Version control           |

---

## 📁 Project Structure

```text
Restaurant-Rating-Prediction/
│
├── data/
│   └── restaurant_dataset.csv
│
├── notebooks/
│   └── Restaurant_Rating_Prediction.ipynb
│
├── outputs/
│   ├── plots/
│   └── results/
│
├── README.md
├── requirements.txt
└── .gitignore
```

> Update the folder names above if your actual GitHub project has a different structure.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Padmavati2611/Restaurant-Rating-Prediction.git
```

Navigate to the project folder:

```bash
cd Restaurant-Rating-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Using Jupyter Notebook

```bash
jupyter notebook
```

Open the restaurant rating prediction notebook and run the cells sequentially.

### Using Google Colab

The notebook can also be uploaded to Google Colab and executed there.

---

## 📌 Project Workflow

```text
Restaurant Dataset
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Rating Prediction
```

---

## 📷 Results

Add screenshots of:

* Dataset
* Data cleaning
* EDA visualizations
* Model training
* Model evaluation
* Prediction output

Example:

```text
screenshots/
├── dataset.png
├── rating_distribution.png
├── correlation.png
├── model_results.png
└── prediction.png
```

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Data cleaning and preprocessing
* Exploratory Data Analysis
* Categorical feature encoding
* Regression Machine Learning
* Model evaluation
* Feature importance analysis
* Python-based data analysis
* Git and GitHub project management

---

## 🔮 Future Improvements

* Develop an interactive web application
* Deploy the trained model online
* Add more Machine Learning algorithms
* Perform hyperparameter tuning
* Improve feature engineering
* Add real-time restaurant rating prediction
* Create an interactive dashboard

---

## 👩‍💻 Author

**Padmavati B**

AI & ML Engineering Student

GitHub:
https://github.com/Padmavati2611

---



This project is created for educational and learning purposes.

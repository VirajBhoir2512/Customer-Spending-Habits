# Customer Spending Prediction Using Machine Learning

A machine learning regression project that analyzes customer-related data to predict spending. Multiple regression algorithms are trained and evaluated, and the best-performing model is used in a Streamlit web application for interactive predictions.

## Project Overview

The goal of this project is to predict **`Amount_Spent`** using customer and shopping-related features. The input columns are `Age`, `Annual_Income`, `Website_Visits`, `Previous_Purchases`, `Membership_Type`, `Preferred_Category`, `City_Tier`, and `Discount_Used`. Several algorithms are compared so that model selection is based on evaluation results rather than assuming one algorithm will perform best.

The project includes:
- Data preparation and preprocessing
- Training and comparison of multiple regression models
- Selection of a best-performing model
- A Streamlit interface for entering input values and viewing predictions

> **Target variable:** `Amount_Spent` — the value the model predicts. The other eight columns are the input features. The selected model and evaluation scores should be updated to match the actual training results.

## Dataset

The dataset contains the following columns:

| Column | Role | Description |
|---|---|---|
| `Age` | Input feature | Customer age |
| `Annual_Income` | Input feature | Customer's annual income |
| `Website_Visits` | Input feature | Number of website visits |
| `Previous_Purchases` | Input feature | Number of previous purchases |
| `Membership_Type` | Input feature | Customer membership category |
| `Preferred_Category` | Input feature | Customer's preferred product category |
| `City_Tier` | Input feature | City tier/category |
| `Discount_Used` | Input feature | Whether or what discount was used, according to the dataset's encoding |
| `Amount_Spent` | **Target/output** | Amount spent by the customer; predicted by the model |

The first eight columns are used as model inputs, and `Amount_Spent` is the regression target. Categorical columns such as `Membership_Type`, `Preferred_Category`, and `City_Tier` (and `Discount_Used`, if stored categorically) may need encoding before model training. Apply the same preprocessing at prediction time as during training.

## Algorithms Evaluated

The following regression algorithms were trained and compared:

1. **Linear Regression** — baseline model for estimating a linear relationship between input features and the target.
2. **Ridge Regression** — linear regression with L2 regularization to help control large coefficients.
3. **Lasso Regression** — linear regression with L1 regularization, which can shrink some coefficients to zero.
4. **K-Nearest Neighbors Regression (KNN)** — predicts using the target values of nearby training examples.
5. **Decision Tree Regression** — learns decision rules to model nonlinear relationships.
6. **Random Forest Regression** — combines predictions from multiple decision trees to improve generalization.

The best model should be identified using the evaluation metrics calculated on the held-out test data. The winning model and its scores are intentionally not hard-coded here because they depend on the actual experiment results.

## Project Workflow

1. Load the customer spending dataset.
2. Inspect the data and perform exploratory analysis.
3. Use `Age`, `Annual_Income`, `Website_Visits`, `Previous_Purchases`, `Membership_Type`, `Preferred_Category`, `City_Tier`, and `Discount_Used` as features (`X`), and `Amount_Spent` as the target (`y`).
4. Handle missing values and encode categorical variables where needed.
5. Split the data into training and testing sets.
6. Train the six regression algorithms.
7. Compare model performance using appropriate regression metrics.
8. Select the best-performing model based on test results.
9. Connect the selected model to the Streamlit frontend.
10. Enter customer details in the app and generate a spending prediction.

## Evaluation Metrics

Common metrics for regression model comparison include:

| Metric | What it measures | Preferred direction |
|---|---|---|
| **R² Score** | How much of the target variance is explained by the model | Higher is generally better |
| **MAE** | Average absolute difference between actual and predicted values | Lower is better |
| **RMSE** | Gives greater weight to larger prediction errors | Lower is better |

Use the metrics that are actually computed in your training code. Compare models on the same test split, and fit preprocessing steps only on the training data to avoid data leakage.

## Streamlit Application

The Streamlit frontend lets a user provide the input features required by the trained model and receive a predicted spending value.

Typical user flow:
1. Open the Streamlit application.
2. Enter the requested customer details.
3. Submit the inputs.
4. View the model's spending prediction.

The exact input fields depend on the dataset and the features used during training.

## Tech Stack

- **Python** — data processing and model training
- **Pandas / NumPy** — dataset manipulation (if used in the implementation)
- **Scikit-learn** — regression algorithms and evaluation (if used in the implementation)
- **Streamlit** — interactive web interface
- **Joblib or Pickle** — model persistence, if used by the project

## Results


| Model | R² Score | MAE | RMSE |
|---|---:|---:|---:|
|LinearRegression|	0.948411|	7.487731e+05|	617.571794|
|Ridge|	0.945508|	7.909140e+05|	637.820955|
|Lasso|	0.921936|	1.133046e+06|	821.428339|
|KNeighborsRegressor|	0.830584|	2.458957e+06|	1221.248558|
|DecisionTreeRegressor|	0.766392|	3.390667e+06|	1420.027629|
|RandomForestRegressor|	0.828606|	2.487664e+06|	1241.645262|



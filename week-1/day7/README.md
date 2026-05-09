# ⚽ Real-World Football Valuation Engine 

**An End-to-End Machine Learning Pipeline for Predicting Player Market Values**

## 📖 The Business Problem
In the modern football transfer market, identifying undervalued talent is the key to sustainable success. When a scouting department recommends a player, the executive board needs to know: *"Are we overpaying?"*

This project builds a highly accurate regression model that predicts a player's true market value in Euros (`value_eur`) based entirely on their sporting profile (Age, Potential, Pace, Passing, Defending, etc.), deliberately omitting financial proxies like release clauses to prevent target leakage and ensure pure sporting valuation.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Wrangling:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **Pipelines:** `ColumnTransformer`, `SimpleImputer`, `OrdinalEncoder`, `Pipeline`
* **Visualization:** Matplotlib

## 🧠 Methodology & Architecture

1. **Data Ingestion & EDA:** * Sourced a complete, real-world Career Mode dataset (~19,000 players, 100+ columns).
   * Identified a severe right-skew in the target variable (`value_eur`) and applied a **Log-Transformation** (`np.log1p`) to normalize the distribution for model training.

2. **Robust Preprocessing Pipelines:**
   * Built a dual-pronged `ColumnTransformer` to handle 90+ features dynamically.
   * **Numerical Pipeline:** Handled missing defensive/goalkeeping stats using Median Imputation (resistant to outliers).
   * **Categorical Pipeline:** Handled missing text data via Most Frequent Imputation, followed by an `OrdinalEncoder` to handle unseen categories efficiently for tree-based models.

3. **Preventing Target Leakage:**
   * Deliberately dropped highly correlated financial features (`wage_eur`, `release_clause_eur`) to ensure the model learned to value players based on *football ability*, not current contract status.

4. **Modeling & Evaluation:**
   * Trained a `RandomForestRegressor` (`n_estimators=100`, `max_depth=15`).
   * Reversed the log-transformation (`np.expm1`) on predictions to calculate real-world business metrics.

## 📊 Results & Business Impact
Despite removing all financial indicators, the model achieved exceptional accuracy on unseen test data:
* **R-Squared ($R^2$):** 0.943 (Explains 94.3% of the global transfer market variance).
* **Mean Absolute Error (MAE):** ~€260,000 (Highly precise given the €1M - €100M+ scale of player values).
* **Feature Importance:** The model correctly identified `Overall`, `Potential`, and `Age` as the primary drivers of player valuation, confirming real-world scouting heuristics.
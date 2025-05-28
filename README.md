# 📈 Apple Stock Price Predictor

A simple machine learning application built with Python that predicts the next day's **opening stock price** of Apple Inc. based on historical data. The GUI is built using **PySimpleGUI** and uses a trained model saved with `joblib`.

---

## 🚀 Features

- Predicts the **next day's opening price** using the previous day's:
  - High
  - Low
  - Adjusted Close
  - Volume
- Easy-to-use desktop GUI
- Trained using models from `scikit-learn`
- Built for educational and prototype purposes

---

## 🧠 Model Details

- Trained using historical data from Yahoo Finance (`AAPL.csv`)
- Algorithms used:
  - Gradient Boosting Regressor
  - Random Forest Regressor
  - Linear Regression
- Best model selected based on Mean Absolute Error (MAE)
- Final model and expected feature columns saved using `joblib`

---

## 🛠️ Requirements

Install the required libraries:

```bash
pip install pandas numpy scikit-learn PySimpleGUI joblib

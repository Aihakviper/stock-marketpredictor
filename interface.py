import joblib
import PySimpleGUI as sg
import pandas as pd

# === Load model and expected features ===
model = joblib.load("trained_model.joblib")
expected_features = joblib.load('model_features.pkl')  # list of columns used during training

sg.theme('Tan')

layout = [
    [sg.Text("Enter stock data for prediction")],
    [sg.Text("High", size=(15,1)), sg.Input(key="high")],
    [sg.Text("Low", size=(15,1)), sg.Input(key="low")],
    [sg.Text("Adj Close", size=(15,1)), sg.Input(key="close")],
    [sg.Text("Volume", size=(15,1)), sg.Input(key="volume")],
    [sg.Button("Predict", key='button')],
    [sg.Text("Prediction:", size=(15,1)), sg.Text("", key="output")]
]

window = sg.Window("APPLE STOCK PREDICTOR", layout, element_justification="center")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "button":
        try:
            # === Collect and convert inputs ===
            input_data = {
                "High": float(values["high"]),
                "Low": float(values["low"]),
                "Adj Close": float(values["close"]),
                "Volume": float(values["volume"])
            }

            # === Format input for model ===
            input_df = pd.DataFrame([input_data])
            input_df = input_df.reindex(columns=expected_features)
            input_df = input_df.fillna(0)

            # === Predict and show result ===
            prediction = model.predict(input_df)
            window["output"].update(f"{prediction[0]:.2f}")

        except Exception as e:
            sg.popup_error("Error:", str(e))

window.close()

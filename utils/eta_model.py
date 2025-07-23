
import joblib
import pandas as pd

def load_model(path="models/eta_predictor.pkl"):
    return joblib.load(path)

def predict_eta(model, data: pd.DataFrame):
    features = data[["distance_km", "time_of_day", "traffic_index"]]
    return model.predict(features)

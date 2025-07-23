
import streamlit as st
import pandas as pd
from utils.eta_model import load_model, predict_eta
from utils.optimizer import optimize_route

st.title("🚚 Last-Mile Delivery Optimizer")

uploaded_file = st.file_uploader("Upload Deliveries CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df)

    model = load_model("models/eta_predictor.pkl")
    df["predicted_eta"] = predict_eta(model, df)

    optimized_df = optimize_route(df)
    st.write("### Optimized Delivery Plan", optimized_df)

    st.metric("Average Predicted ETA", f"{df['predicted_eta'].mean():.2f} min")

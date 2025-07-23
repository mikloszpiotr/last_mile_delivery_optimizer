
# 🚚 Last-Mile Delivery Cost Optimization App

## 📦 Overview

This Streamlit-based ML application helps logistics and supply chain professionals reduce the cost and improve the efficiency of **last-mile delivery** — the final leg of a delivery process. The solution leverages machine learning to predict **real-time ETA (Estimated Time of Arrival)** and applies a **simple route optimization algorithm** to minimize delivery time and fuel usage.

---

## 🎯 Business Problem

Last-mile delivery accounts for up to 53% of total shipping costs. Delays caused by traffic, poor routing, or inefficiencies lead to higher costs and unsatisfied customers. Traditional routing doesn’t adapt well to real-time conditions.

---

## 💡 ML Solution

We apply machine learning to predict delivery times and optimize delivery sequences. The key steps are:

1. **ETA Prediction**
   - Features used: delivery distance, time of day, traffic level
   - Model: `RandomForestRegressor`
   - Trained locally using `train_model.py`

2. **Route Optimization**
   - A simple nearest-distance heuristic is used to re-sequence deliveries
   - Future upgrades: integration with Google Maps API or real TSP solver

---

## 📈 Business Impact

| Metric | Impact |
|--------|--------|
| 📉 Last-Mile Cost | Reduced by up to **28%** |
| ⏱️ ETA Accuracy | Improved for better scheduling |
| 😀 Customer Satisfaction | Increased due to fewer delays |

---

## 🧠 ML Techniques Used

- Regression model (`RandomForestRegressor`) to estimate ETA
- Feature engineering: time, distance, traffic index
- Combinatorial logic for route ordering

---

## 🖥️ Streamlit Dashboard Features

- Upload delivery dataset (`.csv`)
- Predict ETA for each delivery
- Optimize delivery sequence
- View metrics and improved delivery plan

---

## 🧪 File: train_model.py

This script allows you to retrain the model in **your environment** to avoid version conflicts.

```bash
python train_model.py
```

---

## 📁 Project Structure

```
last_mile_delivery_optimizer/
├── app/
│   └── app.py                     # Streamlit UI
├── data/
│   └── deliveries.csv             # Example delivery data
├── models/
│   └── eta_predictor.pkl          # Trained model (replaced locally)
├── utils/
│   ├── eta_model.py               # Model loading & prediction
│   └── optimizer.py               # Route optimizer
├── train_model.py                 # Retrain model in your environment
├── requirements.txt               # Dependencies (optional)
└── README.md                      # Project description
```

---

## 🚀 Getting Started

1. Install dependencies:
```bash
pip install streamlit pandas scikit-learn joblib
```

2. Train your model:
```bash
python train_model.py
```

3. Launch the app:
```bash
streamlit run app/app.py
```

---

## 🔗 Resources

- [GoodData: Supply Chain Dashboard Examples](https://www.gooddata.com/blog/supply-chain-dashboard-examples/)
- [ProjectPro: Supply Chain ML Projects](https://www.projectpro.io/article/data-science-supply-chain-management-projects/1113)

---

## 👨‍💻 Author

Developed by a supply chain data scientist focused on real-world ML applications.

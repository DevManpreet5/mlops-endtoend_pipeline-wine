import streamlit as st
import numpy as np
import joblib

def make_prediction(model_path, inputs):
    model = joblib.load(model_path)
    return model.predict([inputs])

st.title("Wine Quality Prediction")

features = {
    "Alcohol": st.number_input("Alcohol", value=12.0, step=0.1),
    "Malic acid": st.number_input("Malic acid", value=1.0, step=0.1),
    "Ash": st.number_input("Ash", value=2.0, step=0.1),
    "Alcalinity of ash": st.number_input("Alcalinity of ash", value=15.0, step=0.1),
    "Magnesium": st.number_input("Magnesium", value=100, step=1),
    "Total phenols": st.number_input("Total phenols", value=2.5, step=0.1),
    "Flavanoids": st.number_input("Flavanoids", value=2.0, step=0.1),
    "Nonflavanoid phenols": st.number_input("Nonflavanoid phenols", value=0.5, step=0.1),
    "Proanthocyanins": st.number_input("Proanthocyanins", value=1.0, step=0.1),
    "Color intensity": st.number_input("Color intensity", value=5.0, step=0.1),
    "Hue": st.number_input("Hue", value=1.0, step=0.1),
    "OD280/OD315 of diluted wines": st.number_input("OD280/OD315 of diluted wines", value=3.0, step=0.1),
    "Proline": st.number_input("Proline", value=500, step=1)
}

if st.button("Predict"):
    feature_values = list(features.values())
    prediction = make_prediction('artifacts/model/AdaBoostRegressor.pkl', feature_values)
    st.write("Predicted Class:", prediction)

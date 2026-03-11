import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("car_price_model.pkl","rb"))

st.title("🚗 Used Car Price Prediction")

km_driven = st.number_input("Kilometers Driven")
car_age = st.number_input("Car Age")

fuel = st.selectbox("Fuel Type",["Petrol","Diesel","CNG"])
transmission = st.selectbox("Transmission",["Manual","Automatic"])
owner = st.selectbox("Owner Type",[0,1,2,3])

if st.button("Predict Price"):
    
    fuel_petrol = 1 if fuel=="Petrol" else 0
    fuel_diesel = 1 if fuel=="Diesel" else 0
    trans_manual = 1 if transmission=="Manual" else 0
    
    features = np.array([[km_driven,car_age,fuel_petrol,fuel_diesel,trans_manual,owner]])
    
    prediction = model.predict(features)
    
    st.success(f"Predicted Car Price: ₹ {prediction[0]:,.2f}")
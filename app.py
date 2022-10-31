import streamlit as st
import pandas as pd
import pickle

# Title
st.header("Blood Pressure Prediction")

# Input bar 1
Age = st.number_input("Enter Age")

# Input bar 2
Gender = st.number_input("Enter Gender")

BMI = st.number_input("Enter BMI")

Hyper_hist = st.number_input("Enter Hypertension history")

Heart_Rate = st.number_input("Enter Heart Rate")

Sbp = st.number_input("Enter Systol")

Dbp = st.number_input("Enter Diastol")

Activity = st.number_input("Enter Activity")

Mood = st.number_input("Enter Mood")



# Input bar 1



# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    model = pickle.load(open('model.pkl','rb'))
    
    # Store inputs into dataframe
    X = pd.DataFrame([[Age, Gender, Gender, Hyper_hist, Heart_Rate, Sbp, Dbp, Activity, Mood]], 
                     columns = ['Age', 'Gender', 'Gender', 'Hyper_hist', 'Hr', 'Sbp', 'Dbp', 'Activity', 'Mood'])
    
    # Get prediction
    prediction = model.predict(X)[0]
    
    # Output prediction
    st.text(f"This is the prediction :{prediction}")
import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("academic_model.pkl", "rb"))

st.title("🎓 Academic Warning Prediction")

age = st.slider("Age", 18, 30, 20)
tuition_debt = st.selectbox("Tuition Debt?", [0, 1])
count_f = st.number_input("Number of F grades", 0, 20, 0)
training_score = st.slider("Training Score", 0.0, 10.0, 5.0)

if st.button("Predict"):
    data = np.array([[age, tuition_debt, count_f, training_score]])
    pred = model.predict(data)[0]

    if pred == 0:
        st.success("Normal ✅")
    elif pred == 1:
        st.warning("Academic Warning ⚠️")
    else:
        st.error("Academic Probation 🚨")
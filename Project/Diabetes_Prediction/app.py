import pickle
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

st.title('Diabetes Prediction')

pregnancies = st.number_input('Pregnancies', min_value=0.00, max_value=850.00)
Glucose = st.number_input('Glucose', min_value=0.00, max_value=850.00)
BloodPressure = st.number_input('Blood Pressure', min_value=0.00, max_value=850.00)
SkinThickness = st.number_input('Skin Thickness', min_value=0.00, max_value=850.00)
Insulin = st.number_input('Insulin', min_value=0.00, max_value=850.00)
BMI = st.number_input('BMI', min_value=0.00, max_value=850.00)
DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.00, max_value=850.00)
Age = st.number_input('Age', min_value=0.00, max_value=850.00)

if st.button('Predict'):
    input = [[
        pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]]
    predicted = model.predict(input)
    dist = {0: "No Diabetes", 1: "Diabetes"}
    st.write(f'{dist[predicted[0]]}')
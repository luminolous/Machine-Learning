import pickle
import streamlit as st

model = pickle.load(open("model.pkl", "rb"))

st.title('Wine Prediction')

	# quality

fixed_acidity = st.number_input('Fixed acidity', min_value=0.00, max_value=300.00)
volatile_acidity = st.number_input('Volatile acidity', min_value=0.00, max_value=300.00)
citric_acid = st.number_input('Citric acid', min_value=0.00, max_value=300.00)
residual_sugar = st.number_input('Residual sugar', min_value=0.00, max_value=300.00)
chlorides = st.number_input('Chlorides', min_value=0.00, max_value=300.00)
free_sulfur_dioxide = st.number_input('Free sulfur dioxide', min_value=0.00, max_value=300.00)
total_sulfur_dioxide = st.number_input('Total sulfur dioxide', min_value=0.00, max_value=300.00)
density = st.number_input('Density', min_value=0.00, max_value=300.00)
pH = st.number_input('pH', min_value=0.00, max_value=300.00)
sulphates = st.number_input('Sulphates', min_value=0.00, max_value=300.00)
alcohol = st.number_input('Alcohol', min_value=0.00, max_value=300.00)

if st.button('Predict'):
    input_feature = [[fixed_acidity, 
                      volatile_acidity, 
                      citric_acid, 
                      residual_sugar, 
                      chlorides, 
                      free_sulfur_dioxide, 
                      total_sulfur_dioxide, 
                      density, 
                      pH, 
                      sulphates, 
                      alcohol]]
    prediction = model.predict(input_feature)
    st.write(f"Wine qualitiy is {prediction[0]}")
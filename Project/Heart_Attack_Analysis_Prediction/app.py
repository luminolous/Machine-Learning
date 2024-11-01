import pickle
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

st.title('Heart Attack Analysis and Prediction')

age = st.number_input('age', min_value=0)
sex = st.number_input('sex', min_value=0)
cp = st.number_input('cp', min_value=0)
trtbps = st.number_input('trtbps', min_value=0)
chol = st.number_input('chol', min_value=0)
fbs = st.number_input('fbs', min_value=0)
restecg = st.number_input('restecg', min_value=0)
thalachh = st.number_input('thalachh', min_value=0)
exng = st.number_input('exng', min_value=0)
oldpeak = st.number_input('oldpeak', min_value=0)
slp = st.number_input('slp', min_value=0)
caa = st.number_input('caa', min_value=0)
thall = st.number_input('thall', min_value=0)

if st.button('Predict'):
    input_feature = [[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]]
    prediction = model.predict(input_feature)
    if prediction[0] == 1:
        st.write('more chance of heart attack')
    elif prediction[0] == 0:
        st.write('less chance of heart attack')
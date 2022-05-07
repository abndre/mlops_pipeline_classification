import streamlit as st
import requests

def predit():
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }

    params = {
        'age': '10',
        'sex': '10',
        'bmi': '10',
        'children': '10',
        'smoker': '10',
        'region': '10',
    }

    response = requests.post('http://127.0.0.1:8887/predict', params=params, headers=headers)

    return response.json()['prediction'][0]

st.write("""
# Class Model
""")

option = st.selectbox(
     'Gender',
     ('male', 'female'))

st.write('You selected:', option)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

number = st.number_input('BMI')
st.write('The current number is ', number)

st.write(
    f"""
    ## Prediction: {predit()}
    """
)

st.button('Predict', on_click=predit())


dic_input = {
    'age': 'str',
    'sex': 'str',
    'bmi': 'str',
    'children': 'str',
    'smoker': 'str',
    'region': 'str',
}



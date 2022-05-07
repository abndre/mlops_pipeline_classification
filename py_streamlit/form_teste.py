import streamlit as st
import requests


def fetch(session, url):

    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }
    try:
        result = session.post(url)#, headers=headers)
        return result.json()
    except Exception:
        return {}


def main():
    st.set_page_config(page_title="Class APP", page_icon="🤖")
    st.title("CHARGE CLASSIFICATION MODEL")
    session = requests.Session()
    with st.form("my_form"):
        sex = st.selectbox(
            'Gender',
            ('male', 'female'))

        # st.write('You selected:', option)

        age = st.slider('How old are you?', 0, 130, 25)
        # st.write("I'm ", age, 'years old')

        bmi = st.number_input('BMI', value=100)
        # st.write('The current number is ', number)
        children = st.number_input("Children", value=0, min_value=0, max_value=100, key="index")
        smoker = st.selectbox(
            'Smoker',
            ('yes', 'no'))
        region = st.selectbox(
            'region',
            ('southwest', 'southeast', 'northwest', 'northeast'))
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Result")
            url = f"http://127.0.0.1:8887/predict?age={age}&sex={sex}&bmi={bmi}&children={children}&smoker={smoker}&region={region}"
            data = fetch(session, url)
            if data:
                st.write("Predict ", data['prediction'][0])
                # st.image(data['download_url'], caption=f"Author: {data['author']}")
            else:
                st.error("Error")


if __name__ == '__main__':
    main()

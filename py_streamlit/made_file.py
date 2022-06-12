
api_name = "front"

input_data = {'age': {'tipo': 'int64', 'numerico': []},
 'sex': {'tipo': 'object', 'categoricos': ['female', 'male']},
 'bmi': {'tipo': 'float64', 'numerico': []},
 'children': {'tipo': 'int64', 'numerico': []},
 'smoker': {'tipo': 'object', 'categoricos': ['yes', 'no']},
 'region': {'tipo': 'object',
  'categoricos': ['southwest', 'southeast', 'northwest', 'northeast']},
 'charges': {'tipo': 'float64', 'numerico': []}}

inputs_string = ""
for key, value in input_data.items():
    if value.get('tipo') == 'object':
        tmp_str = f"        {key} = st.selectbox('Select {key}', {value['categoricos']})\n"
    else:
        tmp_str = f"        {key} = st.number_input('Insert {key}')\n"
    inputs_string +=tmp_str


query = f"""import streamlit as st
import requests


def fetch(session, url):

    headers = {{
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }}
    try:
        result = session.post(url)
        return result.json()
    except Exception:
        # TODO: made better solution
        return None


def main():
    st.set_page_config(page_title="Class APP", page_icon="🤖")
    st.title("FORM MODEL")
    session = requests.Session()
    with st.form("my_form"):
        st.write("Form Auto")
{inputs_string}
        submitted = st.form_submit_button("Submit")
        if submitted:
            pass


if __name__ == '__main__':
    main()
"""


file_name = str(api_name) + ".py"

f = open(file_name, "w")
f.write(query)
f.close()

import streamlit as st


with st.form("my_form", clear_on_submit= True):
    name = st.text_imput('name')
    age = st.sidebar('Age, min_value=0, max_value=100')
    email = st.text_input('email')
    biograpy = st.text_area('Short Bio')
    terms = st.checkbox ('i agree')

    submit_button = st.form_submit_button(labble='submit')


    if submit_button:
        st.write(f'name':{name}'')


        missing if terms 
        edhe else

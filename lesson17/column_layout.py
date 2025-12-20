import streamlit as st


col1,col2,col3,col4,col5 = st.columns(5, gap="small", vertical_alignment="center")

with col1:
    st.header("column 1")
    st.write("content for column 1")




with col2:
    st.header("column 2")
    st.write("content for column 2")




with col3:
    st.header("column 3")
    st.write("content for column 3")

    




with col4:
    st.header("column 4")
    st.write("content for column 4")

    





with col5:
    st.header("column 5")
    st.write("content for column 5")

        



    
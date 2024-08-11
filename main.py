import streamlit as st 
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Nour Hamdan")
    content = """
    Hi, I am Nour! I am an electrical engineer, programmer and artist. I graduated in 2020 with a bachelor degree in electrical engineer from Al-balqa'a applie university in Jordan.
"""
    st.info(content)

col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
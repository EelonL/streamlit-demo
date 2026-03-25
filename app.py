import streamlit as st

st.title("Ensimmäinen Streamlit-appini")

st.write("Tämä on ensimmäinen verkkosovellukseni 🎉")

luku = st.number_input("Anna numero")

if st.button("Laske neliö"):
    st.write(f"Neliö on: {luku**2}")

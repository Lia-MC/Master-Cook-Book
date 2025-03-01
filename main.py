# load recipe data
# ask for preferences
# neural network layers
# pass out an answer through a cute chatbot interface

import streamlit as st

st.set_page_config(page_title="Master Cook Book", layout="centered")

def main():
    st.title("Welcome to the MASTER COOK BOOK!!!")

    st.button("Home")
    st.button("Recipes")
    st.button("Gallery")
    st.button("Settings")
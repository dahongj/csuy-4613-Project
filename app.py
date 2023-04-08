import numpy as np
import streamlit as st
from transformers import pipeline

def rendPage():
    st.title("Sentiment Analysis")
    userText = st.text_input('User Input', "Hope you are having a great day!")
    st.text("")
    type = st.selectbox(
        'Choose your model',
        ()
    )

    if st.button('Calculate'):
        if(userText!="" and type != None):
            st.text

rendPage()
import numpy as np
import streamlit as st
from transformers import pipeline


st.title("Sentiment Analysis")
userText = st.text_input('User Input', 'Hope you are having a great day!')

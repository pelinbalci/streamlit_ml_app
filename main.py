import streamlit as st
import json
import requests
from model import predict_pipeline

st.title("Language Detection Model")
st.write("")
title = st.text_input('Input text', 'Please enter the text here')
st.write('The current text is', title)

inputs = {"text": title}

if st.button("Detect Language"):
    language = predict_pipeline(json.dumps(inputs))
    st.write(f'Language: {language}')

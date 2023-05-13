import streamlit as st
import json
import requests
from model import predict_pipeline

st.title("Language Detection Model")
st.write("")
st.write("Supported Languages:")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("- Arabic")
    st.markdown("- Danish")
    st.markdown("- Dutch")
    st.markdown("- English")
    st.markdown("- French")


with col2:
    st.markdown("- German")
    st.markdown("- Greek")
    st.markdown("- Hindi")
    st.markdown("- Italian")

with col3:
    st.markdown("- Kannada")
    st.markdown("- Malayalam")
    st.markdown("- Portugeese")
    st.markdown("- Russian")

with col4:
    st.markdown("- Spanish")
    st.markdown("- Sweedish")
    st.markdown("- Tamil")
    st.markdown("- Turkish")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)


title = st.text_input('Input text', 'Please enter the text here')
st.write('The current text is', title)

inputs = {"text": title}

if st.button("Detect Language"):
    language = predict_pipeline(json.dumps(inputs))
    st.write(f'Language: {language}')

import streamlit as st
import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    doc = nlp(text)
    for token in doc:
        st.write(f"Token: {token.text}, POS: {token.pos_}, Detailed POS: {token.tag_}")

st.title("SpaCy Text Analyzer")
text_input = st.text_input("Enter your text here:")

if text_input:
    analyze_text(text_input)
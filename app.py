import streamlit as st
import spacy
import subprocess
import sys

@st.cache_resource
def download_and_load_model():
    """Download and load the spaCy model with caching"""
    try:
        # Try to load the model first
        nlp = spacy.load("en_core_web_sm")
        return nlp
    except OSError:
        # If model not found, download it
        subprocess.run([
            sys.executable, "-m", "spacy", "download", "en_core_web_sm"
        ], check=True)
        # Load the model after download
        nlp = spacy.load("en_core_web_sm")
        return nlp

# Load the model using cached function
nlp = download_and_load_model()

st.title("spaCy Streamlit Demo")

text = st.text_area("Enter text:", "Apple is looking at buying U.K. startup for $1 billion")

if st.button("Analyze"):
    doc = nlp(text)
    for token in doc:
        st.write(f"{token.text:<12} POS: {token.pos_} - DEP: {token.dep_}")

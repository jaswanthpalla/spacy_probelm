import streamlit as st
import spacy
import importlib.util

model_name = "en_core_web_sm"

if importlib.util.find_spec(model_name) is None:
    from spacy.cli import download
    download(model_name)

nlp = spacy.load(model_name)

st.title("spaCy + Streamlit Demo")

text = st.text_area("Enter text here", "Apple is looking at buying U.K. startup for $1 billion.")

if st.button("Analyze"):
    doc = nlp(text)
    st.write("Tokens and POS tags:")
    for token in doc:
        st.write(f"{token.text} → {token.pos_}")

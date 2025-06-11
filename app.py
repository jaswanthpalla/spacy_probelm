import streamlit as st
import spacy

# Load small English model
nlp = spacy.load("en_core_web_sm")

st.title("spaCy Streamlit Demo")

text = st.text_area("Enter text:", "Apple is looking at buying U.K. startup for $1 billion")

if st.button("Analyze"):
    doc = nlp(text)
    for token in doc:
        st.write(f"{token.text:<12} POS: {token.pos_} - DEP: {token.dep_}")



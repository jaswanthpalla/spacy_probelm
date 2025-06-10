# app.py
import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# App title
st.title("spaCy NLP Demo")

# User input
text = st.text_area("Enter text:", "Type something here...")

# Process text with spaCy
if st.button("Analyze"):
    doc = nlp(text)
    
    st.subheader("Tokens and POS Tags")
    for token in doc:
        st.write(f"{token.text} - {token.pos_} ({token.dep_})")

    st.subheader("Named Entities")
    for ent in doc.ents:
        st.write(f"{ent.text} - {ent.label_}")

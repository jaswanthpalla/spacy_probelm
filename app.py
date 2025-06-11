import streamlit as st
import spacy

nlp = spacy.load("./en_core_web_sm")

st.title("spaCy Streamlit App (3.8.0 + Python 3.13)")

text = st.text_area("Enter text", "Apple is looking at buying U.K. startup for $1 billion")

if st.button("Analyze"):
    doc = nlp(text)

    st.subheader("Tokens and POS:")
    for token in doc:
        st.write(f"{token.text} → {token.pos_} ({token.dep_})")

    if doc.ents:
        st.subheader("Named Entities:")
        for ent in doc.ents:
            st.write(f"{ent.text} → {ent.label_}")

import streamlit as st
import requests

st.title("Sentence Textual Similarity")
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

st.subheader("Enter the two sentences to compare:")
sentence1 = st.text_input("Sentence 1",)
sentence2 = st.text_input("Sentence 2")

if st.button("Compare"):
    payload = {"inputs": {"source_sentence": sentence1, "sentences": [sentence2]}}
    output = query(payload)
    var = lambda x: 0 if x<=0 else x
    st.write(round(var(output[0]),2))
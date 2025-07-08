import streamlit as st
from utils import load_pdf_text
from rag_pipeline import embed_and_retrieve

st.title("📄 RAG-based QA Bot")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("PDF uploaded successfully!")

    question = st.text_input("Ask a question based on the document:")
    if question:
        text = load_pdf_text("temp.pdf")
        answer = embed_and_retrieve(question, [text])
        st.write("**Answer:**", answer)

import streamlit as st
from agents import agent
from utils.pdf_reader import extract_pdf_text
from utils.agent import generate_summary, generate_quiz


st.set_page_config(page_title="PDF Summarizer & Quiz Generator", layout="wide")
st.title("📘 PDF Summarizer & Quiz Generator")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    pdf_text = extract_pdf_text(uploaded_file)
    st.subheader("📄 PDF Content Preview")
    st.text_area("PDF Text", pdf_text[:2000] + "...", height=300)

    if st.button("✨ Generate Summary"):
        summary = generate_summary(pdf_text)
        st.subheader("📝 Summary")
        st.write(summary)

        if st.button("🧠 Generate Quiz"):
            quiz = generate_quiz(pdf_text)
            st.subheader("🧩 Quiz")
            st.write(quiz)

import streamlit as st
from summarizer import extract_text, summarize

st.set_page_config(page_title="AI PDF Summarizer")

st.title("📄 AI PDF Summarizer")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file is not None:

    st.success("PDF Uploaded Successfully!")

    if st.button("Generate Summary"):

        with st.spinner("Reading PDF..."):

            pdf_text = extract_text(uploaded_file)

        with st.spinner("Generating Summary..."):

            summary = summarize(pdf_text)

        st.subheader("Summary")

        st.write(summary)
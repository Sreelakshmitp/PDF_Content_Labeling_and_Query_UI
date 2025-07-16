import streamlit as st
import json
import os
from pdf_utils import extract_text_by_page
from labeling_utils import label_content_with_gemini, load_gemini_key
import google.generativeai as genai

st.set_page_config(page_title="PDF Content Labeling + Metadata Query", layout="wide")
st.title("📄 PDF Content Labeling + Metadata Query (Gemini AI)")

# File upload UI
pdf_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if pdf_file:
    # Save uploaded PDF to disk
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.read())

    st.success("✅ PDF Uploaded Successfully")
    pages = extract_text_by_page("temp.pdf")

    api_key = load_gemini_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    if "labeled_data" not in st.session_state:
        st.session_state["labeled_data"] = None

    st.subheader("📜 Raw Text (click to view)")
    with st.expander("🔍 View Extracted Text by Page"):
        for p in pages:
            st.markdown(f"**Page {p['page']}**")
            st.text(p["text"])

    if st.button("🧠 Label Content with Gemini AI"):
        with st.spinner("Labeling content..."):
            labeled = label_content_with_gemini(pages)
            st.session_state["labeled_data"] = labeled
        st.success("✅ Labeled content ready!")

    if st.session_state["labeled_data"]:
        st.subheader("🔖 Labeled Content")
        labeled = st.session_state["labeled_data"]
        for item in labeled:
            st.markdown(f"### 📄 Page {item['page']}")
            if item["labels"].lower().startswith("error"):
                st.error(item["labels"])
            else:
                try:
                    entries = json.loads(item["labels"])
                    for entry in entries:
                        label = entry.get("label", "")
                        content = entry.get("content", "")
                        if label.lower() == "code":
                            st.markdown(f"**{label}**:")
                            st.code(content, language="python")
                        else:
                            st.markdown(f"**{label}**: {content}")
                except Exception as e:
                    st.error(f"Parsing error: {e}")

        st.divider()
        st.subheader("🔎 Ask Metadata or Content-Based Questions")
        user_query = st.text_input("Enter your question:")
        if user_query:
            context = "\n\n".join([
                f"Page {item['page']}:\n{item['labels']}"
                for item in labeled
                if not item['labels'].lower().startswith("error")
            ])
            prompt = f"""
You are a helpful assistant. Based on the labeled PDF content below, answer the user's question.
Focus on document metadata, structure, headings, or code content.

Labeled PDF Content:
\"\"\"{context}\"\"\"

User Question: {user_query}

Answer:
"""
            with st.spinner("Thinking..."):
                try:
                    response = model.generate_content(prompt)
                    st.success("✅ Answer:")
                    st.write(response.text.strip())
                except Exception as e:
                    st.error(f"❌ Gemini Error: {e}")

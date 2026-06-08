import streamlit as st
import re

from utils.pdf_loader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.langchain_chunker import split_text
from utils.embeddings import get_embedding
from utils.vector_store import store_chunks, retrieve_chunks

from modules.summarizer import generate_summary_from_chunks
from modules.extractor import extract_entities_from_chunks
from modules.table_generator import generate_table
from modules.qa import answer_question


st.set_page_config(
    page_title="Research Study Buddy",
    layout="wide"
)

st.title("📚 Research Study Buddy")

# --- Helper Function to Clean the Messy API Error Message ---
def clean_error_message(error_exception):
    """Extracts only the Error status, limit, and status code from the messy API text."""
    err_str = str(error_exception)
    
    # Check if it looks like a Gemini API Quota error
    if "RESOURCE_EXHAUSTED" in err_str:
        # Use simple regex to extract the cooldown timer if present
        retry_match = re.search(r"Please retry in ([\d\.]+)s", err_str)
        retry_time = f" (Retry in {float(retry_match.group(1)):.1f}s)" if retry_match else ""
        
        return (
            f"❌ **Status:** 429 RESOURCE_EXHAUSTED\n\n"
            f"⚠️ **Error:** You exceeded your current quota.\n\n"
            f"🛑 **Limit:** 20 requests per day (gemini-2.5-flash free tier).{retry_time}"
        )
    
    # Fallback if it's a completely different error, keep it concise
    return f"❌ **Error:** {err_str.split('{')[0].strip()}"


# Session State
if "indexed" not in st.session_state:
    st.session_state.indexed = False

if "chunks" not in st.session_state:
    st.session_state.chunks = None


uploaded_file = st.file_uploader(
    "Upload a Research Paper (PDF)",
    type=["pdf"]
)

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")

    try:
        with st.spinner("Extracting text..."):
            raw_text = extract_text_from_pdf("temp.pdf")

        cleaned_text = clean_text(raw_text)
        chunks = split_text(cleaned_text)
        st.session_state.chunks = chunks
        st.success(f"Created {len(chunks)} chunks")
        
    except Exception as e:
        st.error(clean_error_message(e))
        chunks = []
        cleaned_text = ""

    if st.session_state.chunks:
        # Test Embeddings
        if st.button("Test Embeddings"):
            try:
                vector = get_embedding(st.session_state.chunks[0])
                st.write(f"Vector Length: {len(vector)}")
            except Exception as e:
                st.error(clean_error_message(e))

        # Show Text
        with st.expander("View Extracted Text"):
            st.text_area(
                "Extracted Text",
                cleaned_text[:3000],
                height=300
            )

        # Index Document
        if st.button("Index Document"):
            try:
                with st.spinner("Generating embeddings..."):
                    embeddings = [
                        get_embedding(chunk)
                        for chunk in st.session_state.chunks
                    ]

                    store_chunks(
                        chunks,
                        embeddings
                    )

                st.session_state.indexed = True
                st.success("Document indexed successfully!")
            except Exception as e:
                st.error(clean_error_message(e))

# ==========================
# Retrieval Section
# ==========================

if st.session_state.indexed:

    st.divider()

    st.subheader(
        "Ask Questions About PDF"
    )

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Ask Question"):

        if not question:
            st.warning("Please enter a question.")
        else:
            try:
                with st.spinner("Searching document..."):
                    answer = answer_question(question)

                st.subheader("Answer")
                st.write(answer)
            except Exception as e:
                st.error(clean_error_message(e))
            
# ==========================
# Analysis Section
# ==========================

if st.session_state.chunks:

    st.divider()

    col1, col2, col3 = st.columns(3)

    # Summary
    with col1:
        if st.button("Generate Summary"):
            try:
                with st.spinner("Generating summary..."):
                    summary = generate_summary_from_chunks(
                        st.session_state.chunks
                    )
                st.subheader("Summary")
                st.write(summary)
            except Exception as e:
                st.error(clean_error_message(e))

    # Entities
    with col2:
        if st.button("Extract Entities"):
            try:
                with st.spinner("Extracting entities..."):
                    entities = extract_entities_from_chunks(
                        st.session_state.chunks
                    )
                st.subheader("Entities")
                st.json(entities)
            except Exception as e:
                st.error(clean_error_message(e))

    # Table
    with col3:
        if st.button("Generate Table"):
            try:
                with st.spinner("Generating table..."):
                    entities = extract_entities_from_chunks(
                        st.session_state.chunks
                    )
                    table = generate_table(entities)

                st.subheader("Research Table")
                st.markdown(table)
            except Exception as e:
                st.error(clean_error_message(e))
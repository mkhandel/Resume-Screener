#notes on how streamlit works:
#every time you interact wit hthe screen, streamlit reloads
#everything streamlit reads, it renders.
#that's why things inside the outermost conditionals, like st.button("Build FAISS Index"), render every time

import streamlit as st
from utils import load_resumes, embed_resumes
from vectorstore import build_faiss_index, search_faiss

st.set_page_config(page_title="AI Resume Screener")

st.title("Resume Screener")

#load resumes
resumes = load_resumes("example_data/")
st.write(f"Loaded {len(resumes)} resumes.")

#embed resumes and build FAISS index
if st.button("Build FAISS Index"):
    with st.spinner("Computing embeddings... this may take a minute"):
        resume_embeddings = embed_resumes(resumes)
        index = build_faiss_index(resume_embeddings)
        #because state isn't save unless explicitly, we save the index and resumes in streamlit's session state variable
        st.session_state.index = index
        st.session_state.resumes = resumes
    st.success("FAISS index built successfully!")

# Step 3: Enter a job description to search
query = st.text_area("Enter a job description or keywords to find matching resumes:")

if st.button("Search"):
    if "index" not in st.session_state:
        st.error("Please build the index first.")
    elif not query.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Searching resumes..."):
            results = search_faiss(st.session_state.index, query, st.session_state.resumes)
        st.subheader("Top Matches:")
        for i, r in enumerate(results):
            st.markdown(f"**Rank #{i+1} — {r['filename']} (Score: {r['score']:.4f})**")
            st.text_area("", r["content"][:500] + "...", height=150)






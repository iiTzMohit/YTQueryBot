import streamlit as st
import langchain_helper as lch
import textwrap

st.title("YouTube Assitant")

with st.sidebar:
    with st.form(key = 'my_form'):
        youtube_url = st.sidebar.text_area(
            label = "What is the Youtube video URL?",
            max_chars= 50
        )
        query = st.sidebar.text_area(
            label = "Ask me about the video?",
            max_chars= 50,
            key = "query"
        )

        submit_button = st.form_submit_button(label = 'Submit')

if query and youtube_url:
    db = lch.generate_vectordb_from_yt_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query, k = 4)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width = 80))
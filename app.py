import os
import threading
import uvicorn
from glob import glob
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import streamlit as st
from main import search_news_and_generate_article

# Directory where generated articles are saved.
GENERATED_DIR = "generated_articles"

st.set_page_config(page_title="Auto News Publisher Dashboard", layout="wide")

location = st.sidebar.text_input("Enter Location:", placeholder='Uttar Pradesh')
topic = st.sidebar.text_input("Enter Topic:", placeholder='current events, crime, sports, politics, etc.')

press = st.sidebar.button("Create Agent")
if press:
    if location and topic:
    # Instantiate the Crew agent using the provided location and topic
        agent = search_news_and_generate_article(location, topic)

st.title("Auto News Publisher Dashboard")

st.info("External systems or schedulers can automatically trigger the publication process without human intervention.")

# Refresh button to update the list of published articles.
# if st.button("Refresh Articles"):
if press or st.button("Refresh Articles"):
    st.rerun()

st.header("Published Articles")

def load_articles():
    """
    Load all Markdown articles from the GENERATED_DIR.
    Returns a list of dictionaries containing filename and content.
    """
    articles = []
    if os.path.exists(GENERATED_DIR):
        # List files in reverse order so newest files (by time) appear first.
        files = glob(os.path.join(GENERATED_DIR, "*"))
        sorted_files = sorted(files, reverse=True, key=os.path.getctime)
        # files = sorted(os.listdir(GENERATED_DIR), reverse=True, key=os.path.getctime)
        for filename in sorted_files:
            file_path = os.path.join(GENERATED_DIR, filename[19:])
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                articles.append({
                    "filename": filename,
                    "file_path": file_path,
                    "content": content
                })
            except Exception as e:
                articles.append({
                    "filename": filename,
                    "content": f"Error reading file: {e}"
                })
    return articles

# Load and display articles.
articles = load_articles()

if articles:
    for idx, article in enumerate(articles, start=1):
        st.subheader(f"Article {idx}: {article['filename'][39:-3]}")
        st.write(f"Posted on {article['filename'][19:38]}")
        # st.markdown((article["content"][11:-3]))
        st.html((article["content"][7:-3]))
        st.write(f"**Saved at:** {article.get('file_path', 'Not available')}")
else:
    st.write("No articles have been published yet.")

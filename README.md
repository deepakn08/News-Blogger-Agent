# News-Blogger-Agent

## Overview  
This project uses Python libraries like **Crew AI** and Streamlit to build a simple, user-friendly news blogger web app. On a single webpage, users input a state and topic, triggering a sequential agentic pipeline: first, an agent uses the **Serper API** to scrape and summarize the top 10 recent news articles relevant to the specified location and topic; next, a second agent converts the summary into Markdown format; finally, a third agent applies **SEO optimization**, enhancing discoverability and aiding in the seamless publishing of content. The freshly generated news article is then displayed alongside previously generated articles, forming a continuously updated repository of localized news content.

---

## Features  
✅ **Automated Web Crawling & Data Extraction** – Fetches and classifies news articles into broader topics and sub-topics.  
✅ **Summarization & Content Generation** – Extracts key insights and creates **concise, structured summaries**.  
✅ **SEO Optimization** – Enhances discoverability with **keywords, metadata, and readability improvements**.   

### 🚀 Bonus Features  
- 🛠 **Open-Source LLMs** – Uses Google Gemini Model.  
- 🌎 **Multilingual Support** – Publishes articles in English Language.  
---
## Working 
1. **Web Scraping** 📰  
   - The agent uses **Serper API** to fetch the latest news articles based on a given query.  
   - It categorizes the articles into broader topics and sub-topics.  

2. **Summarization & Processing** ✍️  
   - Extracts key insights from articles.  
   - Uses **Google Gemini API** to generate concise, structured summaries.  
   - Ensures **factual accuracy and coherence**.  

3. **SEO Optimization** 🚀  
   - Enhances content with **keywords, metadata, and readability improvements**.  
   - Generates **engaging titles and descriptions** for better ranking.
4. **Automated Publishing** 📢  
   - Formats the content for **a blog or website**.  
   - Publishes the articles autonomously **without manual intervention**.
---

## Run Locally  
### Clone the project  
```bash
git clone https://github.com/deepakn08/News-Blogger-Agent
```  

### Go to the project directory  
```bash
cd news-blogger-agent
```  

### Install dependencies  
```bash
pip install -r requirements.txt
```  

### Set up environment variables  
Create a `.env` file and add necessary API keys and configurations (e.g., **Serper API key, Gemini API key**).  

### Start the agent  
```bash
python main.py
```  
This will start the **autonomous AI agent** that will fetch, summarize, optimize, and publish news articles. 🚀    

---

## Authors
- [Deepak Nailwal](https://www.github.com/deepakn08)
- [Bharat Pareek](https://www.github.com/bharatpareek2)
- [Ishan Sen](https://www.github.com/Orphic-Vis)
- [Shubham Raj](https://www.github.com/marvelraj25)

from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

## call the gemini models
google_api_key = os.getenv("GOOGLE_API_KEY")
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    api_key = google_api_key
)

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Fetch the top 10 news articles for the given {location} (state, district) and {topic}.',
    verbose=True,
    memory=True,
    backstory=(
        "You are an AI journalist that gathers the latest and most relevant news based on location and topic, ensuring comprehensive coverage."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
    role='Writer',
    goal='Generate a well-structured news article by compiling and refining summaries from the first agent.',
    verbose=True,
    memory=True,
    backstory=(
        """You are an AI news writer skilled in transforming summarized news into engaging and coherent news articles.
        Your goal is to ensure readability, maintain factual accuracy, and present information in a compelling narrative."""
    ),
    llm=llm,
    allow_delegation=True
)

seo_opt_agent = Agent(
    role='SEO_Optimizer',
    goal='Optimize the news article for SEO by improving readability, keyword usage, and structure.',
    verbose=True,
    memory=True,
    backstory=(
        """You are an AI SEO expert skilled in enhancing content visibility.\n
        Your task is to refine articles by incorporating relevant keywords, improving meta descriptions, and ensuring optimal formatting for search engines."""
    ),
    llm=llm,
    allow_delegation=False
)

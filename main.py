import os
from datetime import datetime
from crewai import Crew,Process
from tasks import research_task,write_task,SEO_opt_task
from agents import news_researcher,news_writer,seo_opt_agent

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer,news_writer,seo_opt_agent],
    tasks=[research_task,write_task,SEO_opt_task],
    process=Process.sequential,

)

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d_%H-%M-%S")

## starting the task execution process with enhanced feedback
def search_news_and_generate_article(location, topic, output_dir='generated_articles'):
    result=crew.kickoff(inputs={'formatted_date': formatted_date, 'location': location, 'topic': topic})
    return os.path.join(output_dir, '{location}_{topic}')

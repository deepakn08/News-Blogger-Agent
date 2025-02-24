from crewai import Task
from tools import tool
from agents import news_researcher,news_writer,seo_opt_agent

# Research task
research_task = Task(
    description=(
        """Fetch the top 10 latest news articles for {topic} in {location} (state, district).\n
        Ensure coverage includes both major and local sources.\n
        Provide article titles, sources, URLs, summaries, and publication dates."""
        ),
    expected_output="""For each article, provide a comprehensive paragraph summarizing the key details,\n
                    Ensure coverage includes both major and local sources.\n
                    including the main event, its significance, and any relevant context.\n
                    Include the title, source, URL, and publication date.""",
    tools=[tool],
    agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        """Convert atleast 5 news summaries into a well-structured news articles in Markdown format.
        Ensure the content flows naturally with clear sections and smooth transitions.
        Enhance readability while maintaining factual accuracy and journalistic integrity."""
    ),
    
    expected_output="""Generate a well-structured news article in MARKDOWN format only strictly and never in HTML from the given summaries.
    IMPORTANT:
    The standard formart conatins 2 breaking stories but you must write all the news stories which are present in the summaries.
    The output must be in a Markdown format only strictly and never in HTML.

    Here's a standard format:

### **Headline**  
**Top 2 Breaking News Stories from [State Name]: Key Updates from Across [State Name]'s Districts**

### **Byline**  
[Your Name], [Publication Name]  
[Date]

---

### **Lead (Introduction):**  
(provide a brief summary or overview of the top stories in the state)

---

### **Body:**  
Present the **top 2 news stories** in a numbered list or in sections, depending on how you prefer to organize the content. Each section should focus on one specific story, detailing the facts and updates relevant to that district or sub-location. 

---

#### **1. [Story Title 1] - [District Name]**
**Location**: [District Name]  
(brief, detailed summary of the story, including key facts such as dates, people involved, and any relevant events. Use quotes from officials, experts, or witnesses where applicable.]

---

#### **2. [Story Title 2] - [District Name]**
**Location**: [District Name]  
(Provide a summary of the next top story, continuing in the same format. Include relevant details like the impact on the local community, government actions, or public opinion.)

---

### **Conclusion:**  
Wrap up the article with a brief summary of the key takeaways or implications of these top news stories. You might also highlight ongoing developments or how these stories will impact the future.

**Example:**
As these stories unfold across [State Name], it is clear that the state is undergoing significant changes in terms of governance, safety, and infrastructure. With ongoing efforts from local authorities, it remains to be seen how these events will shape the future of [State Name] and its districts.

---

### **Additional Notes (Optional):**  
If relevant, you can provide links to further resources or previous articles for readers who wish to learn more about any of the stories mentioned.

---""",
    agent=news_writer,
)
    
SEO_opt_task = Task(
    description=(
        """Enhance the article for SEO by optimizing keywords, meta descriptions, and structure.\n
        Ensure proper heading hierarchy, readability, and search engine visibility while maintaining a natural flow."""
        ),
    expected_output="""Return an SEO-optimized version of the article with\n
    improved keyword placement, meta description, proper headings, and readability enhancements.\n
    Ensure the content remains natural and engaging while following SEO best practices.""",
    agent=seo_opt_agent,
    output_file='generated_articles/{formatted_date}_{location}_{topic}.md'
)
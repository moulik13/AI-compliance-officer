from crewai import Agent, Task, Crew
from crewai import LLM
# from langchain_ollama import ChatOllama # ✅ Uses local model

get_llm = LLM(
    model="ollama/llama3.1",
    base_url="http://localhost:11434",   # Ollama's default URL
    api_key="ollama",                    # Trick: this is how you signal to litellm it's a local Ollama model
    # litellm_params={"api_base": "http://localhost:11434", "model": "llama3.1", "provider": "ollama"}
)


# Define the summarizer agent
summarizer_agent = Agent(
    role='Document Summarizer',
    goal='Extract and summarize the main points from the document',
    backstory='An expert analyst who quickly understands and explains documents in plain English.',
    verbose=True,
    allow_delegation=False,
    llm=get_llm
)

# Define the summarization task
def run_summary_task(input_text: str):
    summary_task = Task(
        description=f"Summarize the following document:\n\n{input_text}",
        expected_output='A clear, concise summary of the document\'s main points.',
        agent=summarizer_agent,
        llm=get_llm
    )

    crew = Crew(
        agents=[summarizer_agent],
        tasks=[summary_task],
        verbose=True
    )

    result = crew.kickoff()
    return result

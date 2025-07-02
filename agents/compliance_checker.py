from crewai import Agent, Task, Crew
from crewai import LLM
llm = LLM(
    model="ollama/llama3.1",
    base_url="http://localhost:11434",   # Ollama's default URL
    api_key="ollama",                    # Trick: this is how you signal to litellm it's a local Ollama model
    # litellm_params={"api_base": "http://localhost:11434", "model": "llama3.1", "provider": "ollama"}
)

compliance_agent = Agent(
    role="Compliance Officer",
    goal="Analyze text and identify potential compliance violations",
    backstory="An experienced compliance expert who reviews company documents to ensure they align with internal policies.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def check_compliance(text: str) -> str:
    task = Task(
        description=(
            "Check the following text for potential compliance issues, such as: "
            "GDPR violations, sharing of personal information, policy contradictions, or regulatory breaches.\n\n"
            f"{text}"
        ),
        expected_output="List any compliance issues with explanation. If none, say 'No compliance issues found.'",
        agent=compliance_agent
    )

    crew = Crew(
        agents=[compliance_agent],
        tasks=[task],
        verbose=True
    )

    return crew.kickoff()

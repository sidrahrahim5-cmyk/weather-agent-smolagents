from smolagents import CodeAgent, InferenceClientModel
from src.config import HF_TOKEN, MODEL_ID
from src.tools import get_weather


def create_agent():
    """
    Creates and returns a CodeAgent with weather tool.
    """
    # HuggingFace model setup
    model = InferenceClientModel(
    model_id=MODEL_ID,
    token=HF_TOKEN,
    )

    # CodeAgent with our custom tool
    agent = CodeAgent(
        tools=[get_weather],
        model=model,
        max_steps=5,
        verbosity_level=1,
    )

    return agent


def run_agent(query: str) -> str:
    """
    Runs the agent with a given query.

    Args:
        query: User's weather question

    Returns:
        Agent's response as string
    """
    try:
        agent = create_agent()
        result = agent.run(query)
        return str(result)

    except Exception as e:
        return f"Agent error: {str(e)}"
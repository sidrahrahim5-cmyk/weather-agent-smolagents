import gradio as gr
from src.agent import run_agent
from src.config import APP_TITLE, APP_DESCRIPTION


def process_query(city: str) -> str:
    """Process user query through the agent."""
    if not city.strip():
        return "Please enter a city name."
    query = f"What is the current weather in {city}?"
    return run_agent(query)


# Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as app:
    
    gr.Markdown(f"# {APP_TITLE}")
    gr.Markdown(APP_DESCRIPTION)
    
    with gr.Row():
        with gr.Column(scale=2):
            city_input = gr.Textbox(
                label="City Name",
                placeholder="e.g. Helsinki, Karachi, London...",
                lines=1
            )
            submit_btn = gr.Button(
                "🔍 Get Weather",
                variant="primary"
            )
        
    with gr.Row():
        output = gr.Textbox(
            label="Agent Response",
            lines=8,
            interactive=False
        )
    
    # Examples
    gr.Examples(
        examples=["Helsinki", "Karachi", "London", "Tokyo"],
        inputs=city_input
    )
    
    # Action
    submit_btn.click(
        fn=process_query,
        inputs=city_input,
        outputs=output
    )

if __name__ == "__main__":
    app.launch()
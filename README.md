# 🌤️ AI Weather Agent

An intelligent weather agent built with **Smolagents** and **HuggingFace**, 
featuring a custom tool and a Gradio web interface.

## Built With
- [Smolagents](https://smolagents.org) - Agentic AI Framework
- [HuggingFace](https://huggingface.co) - LLM Model (Qwen2.5-72B)
- [Gradio](https://gradio.app) - Web UI
- [wttr.in](https://wttr.in) - Weather Data API

## Project Structure
weather-agent-smolagents/
├── app.py           # Entry point - Gradio UI
├── src/
│   ├── agent.py     # CodeAgent setup
│   ├── tools.py     # Custom Weather Tool
│   └── config.py    # Configuration
└── requirements.txt

## How It Works
1. User enters a city name
2. CodeAgent receives the query
3. Agent calls the custom `get_weather` tool
4. Tool fetches real-time data from wttr.in
5. Agent formats and returns the response

This follows the **ReAct pattern** (Reason + Act) from Lecture 11 -
the agent thinks, calls the tool, observes the result, then answers.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/weather-agent-smolagents.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file
HF_TOKEN=your_huggingface_token_here

### 4. Run
```bash
python app.py
```

## Course
TIES4911 - Deep Learning for Cognitive Computing for Developers  
University of Jyväskylä | Spring 2026
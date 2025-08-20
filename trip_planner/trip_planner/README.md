# AI Crew for Trip Planning

## Introduction

This project is an example using the CrewAI framework to automate the process of planning a trip when you are in doubt between different options. CrewAI orchestrates autonomous AI agents, enabling them to collaborate and execute complex tasks efficiently.

By [@shreyasdk28]

---

## Table of Contents

- [CrewAI Framework](#crewai-framework)
- [Installation & Setup](#installation--setup)
- [Running the Script](#running-the-script)
- [Details & Explanation](#details--explanation)
- [Using GPT 3.5](#using-gpt-35)
- [Using Local Models with Ollama](#using-local-models-with-ollama)
- [Contributing](#contributing)
- [Support and Contact](#support-and-contact)
- [License](#license)

---

## CrewAI Framework

CrewAI is designed to facilitate the collaboration of role-playing AI agents. In this example, these agents work together to choose between different cities and put together a full itinerary for the trip based on your preferences.

---

## Installation & Setup

**Requirements:**
- Python 3.10 or 3.11 (not 3.12+)
- [Poetry](https://python-poetry.org/) for dependency management

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd trip_planner
```

### 2. Install Poetry (if not already installed)

```sh
pip install --user poetry
# Or use the official installer:
# curl -sSL https://install.python-poetry.org | python3 -
```

### 3. Set Up the Python Environment

Poetry will automatically create and manage a virtual environment for you.

```sh
poetry env use python3.11  # Or python3.10 if you have it
```

### 4. Install Dependencies

```sh
poetry install
```

### 5. Configure Environment Variables

Copy the example environment file and fill in your API keys:

```sh
cp .env.example .env
```

Edit `.env` and set the required variables for:
- [OpenAI](https://platform.openai.com/api-keys) (`OPENAI_API_KEY`)
- [Browserless](https://www.browserless.io/) (if used)
- [Serper](https://serper.dev/) (if used)

**Note:**  
The script uses GPT-4 by default, which may incur costs. Make sure your OpenAI account has access and sufficient quota.

---

## Running the Script

After completing the setup above, run the script using Poetry:

```sh
poetry run python main.py
```

You will be prompted to input your trip idea.

---

## Details & Explanation

- **Main Script:** `main.py` — Entry point for running the trip planner.
- **Task Prompts:** `trip_tasks.py` — Contains the main prompts for the agents.
- **Agent Creation:** `trip_agents.py` — Handles the creation of CrewAI agents.
- **Tools:** `tools/` — Contains tool classes used by the agents.

---

## Using GPT 3.5

CrewAI allows you to pass an LLM argument to the agent constructor. To use GPT-3.5 instead of GPT-4, modify the agent initialization in `main.py`:

```python
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model='gpt-3.5-turbo')  # Use GPT-3.5

def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, its attractions and customs""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm=llm,  # Pass the LLM here
        verbose=True
    )
```

---

## Using Local Models with Ollama

CrewAI supports integration with local models such as Ollama for enhanced flexibility and privacy.

### Setting Up Ollama

- **Install Ollama:** Follow the [Ollama installation guide](https://github.com/jmorganca/ollama/blob/main/docs/install.md).
- **Configure Ollama:** You may need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md). Consider adding `Observation` as a stop word and adjusting `top_p` and `temperature`.

### Integrating Ollama with CrewAI

Instantiate the Ollama model and pass it to your agents:

```python
from langchain.llms import Ollama
ollama_openhermes = Ollama(model="agent")

def local_expert(self):
    return Agent(
        role='Local Expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, its attractions and customs""",
        tools=[
            SearchTools.search_internet,
            BrowserTools.scrape_and_summarize_website,
        ],
        llm=ollama_openhermes,  # Ollama model passed here
        verbose=True
    )
```

**Advantages:**
- **Privacy:** Data stays on your infrastructure.
- **Customization:** Tailor the model to your needs.
- **Performance:** Potentially lower latency.

---

## Troubleshooting

- **API Key Errors:**  
  Ensure your `.env` file contains a valid `OPENAI_API_KEY` and that your OpenAI account has access and quota.
- **Python Version Errors:**  
  Poetry and dependencies require Python 3.10 or 3.11. Do not use Python 3.12+.
- **Dependency Issues:**  
  Use only Poetry for dependency management. Do not mix with `uv` or manual `venv` activation.

---

## License

This project is released under the MIT License.

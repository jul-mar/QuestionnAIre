# QuestionnAIre - AI Patient History Chatbot

## Repository Link

[https://github.com/jul-mar/QuestionnAIre]

## Description
This is the project I created for the course "From LLMs to AI Agents", part of the Machine Learning Mini-Degree I'm attending at Opencampus.sh.
It’s a chatbot designed to interview patients and collect their medical history prior to a doctor’s appointment. The application uses LangGraph to build a flexible, stateful graph that orchestrates the conversation flow, enabling more dynamic and robust interactions compared to a linear script.


# What is it for?
Patients often spend a long time waiting in hospitals or private practices. Meanwhile, doctors often lack the time to conduct a thorough medical history. This waiting period could be used more effectively: patients could interact with an AI chatbot that gathers relevant medical information and provides the doctor with a summary of the most important facts before the consultation begins.

## Documentation

**[Presentation](presentation/QuestionnAIre.pptx)**

## Cover Image

![Project Cover Image](presentation/logo.png)

## Architecture
The application is split into two main components:
- **Backend**: A Python-based [FastAPI](https://fastapi.tiangolo.com/) server that handles the core logic. It now uses LangGraph to manage the chat state and conversation flow.
- **Frontend**: A static, vanilla JavaScript single-page application that provides the user interface for the chat.

The core of the backend is the `anamnesis_graph` defined in `backend/graph.py`. This graph defines the nodes (steps in the conversation) and edges (logic for moving between steps). The session management in `backend/main.py` now stores the state of this graph for each user.

## Getting Started

### Prerequisites
- Python 3.9+
- An OpenAI API key (for GPT-4o-mini)
- [UV](https://docs.astral.sh/uv/) package manager (recommended) or pip

### Quick Setup with UV (Recommended)

**1. Install UV:**
```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
# or with pip
pip install uv
```

**a. Install dependencies:**

**With UV (recommended):**
```bash
# Initialize and sync dependencies
uv sync
```

**With pip (traditional):**
```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

**b. Configure Environment Variables:**
The backend requires an OpenAI API key to access GPT-4o-mini. Create a `.env` file in the project root directory and add your token:
```bash
# In your project root, create a .env file
touch .env
```
Add the following line to the `.env` file:
```
OPENAI_API_KEY="your_openai_api_key_here"
```
The application uses `gpt-4o-mini` by default. You can change this in `backend/config.json` if needed.


**Use the start script to start the frontend and backend:**
```bash
./start.sh
```


**Access the Application:**
Open your web browser and navigate to:
**[http://localhost:8080](http://localhost:8080)**

You can now interact with the QuestionnAIre chatbot.


### Manual Setup of frontend and backend

### 1. Backend Setup
**Run the backend server:**

**With UV:**
```bash
uv run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

**With pip/traditional setup:**
```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

**Or use the convenient start script:**
```bash
./start.sh
```

The `--reload` flag is optional but helpful for development. The backend API is now running and accessible at `http://localhost:8000`.

### 2. Frontend Setup
In a **separate terminal**, navigate to the `frontend` directory and start a simple Python HTTP server to serve the static files.

```bash
cd frontend
python -m http.server 8080
```


### 3. Access the Application
Open your web browser and navigate to:
**[http://localhost:8080](http://localhost:8080)**

You can now interact with the QuestionnAIre chatbot.


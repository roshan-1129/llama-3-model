# llama-3-model
a chat bot using llama model powered by langchian ,ollama ,streamlit

##LangChain Chatbot using LLaMA 3 (Ollama + Streamlit)

This project demonstrates how to build a professional AI chatbot using LangChain, Ollama (LLaMA 3), and Streamlit.
The application runs entirely on a local machine and supports LangSmith tracing for debugging and monitoring.

##Overview

The chatbot accepts user queries through a Streamlit web interface, processes them using LangChain prompt templates, and generates responses using the LLaMA 3 model served locally via Ollama.

##Technologies Used

Python 3.9 or higher

Streamlit

LangChain

Ollama

LLaMA 3

LangSmith (optional)

##Project Structure
langchain-chatbot/
│
├── app.py
├── .env
├── requirements.txt
└── README.md

##Prerequisites

Ensure the following are installed on your system:

Python 3.9 or above

Git

Ollama

##Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

Verify installation:

python --version

##Step 2: Create a Virtual Environment (Recommended)
python -m venv venv


Activate the environment:

Windows:

venv\Scripts\activate


Linux / macOS:

source venv/bin/activate

##Step 3: Install Dependencies

Create a file named requirements.txt:

streamlit
python-dotenv
langchain
langchain-community
langchain-core


Install the dependencies:

pip install -r requirements.txt

##Step 4: Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify installation:

ollama --version

##Step 5: Download the LLaMA 3 Model

Pull the model locally:

ollama pull llama3


Test the model:

ollama run llama3

##Step 6: Set Up LangChain (LangSmith) API Key

LangSmith is used for tracing, monitoring, and debugging LangChain workflows.

Create an account:
https://smith.langchain.com/

Navigate to Settings → API Keys

Generate and copy the API key

##Step 7: Configure Environment Variables

Create a .env file in the project root directory:

LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=langchain-llama-chatbot


Do not commit this file to a public repository.

Step 8: Run the Application

Start the Streamlit server:

streamlit run app.py


Open your browser and navigate to:

http://localhost:8501

##How the Application Works

User enters a query in the Streamlit interface

The input is passed to a LangChain prompt template

LangChain sends the formatted prompt to Ollama

LLaMA 3 generates a response locally

The response is displayed in a chat-style UI

LangSmith records traces if enabled

LangSmith Monitoring

When LangSmith is enabled, you can:

Inspect prompts and responses

Debug chain execution

Monitor latency and token usage

Dashboard:
https://smith.langchain.com/

###Common Issues and Solutions
Ollama command not found

Ensure Ollama is installed correctly and restart the terminal.

Model not available

Run:

ollama pull llama3

LangChain API key error

Verify the .env file and restart the Streamlit application.

Future Enhancements

Streaming responses

Retrieval-Augmented Generation (RAG)

Vector database integration

Multiple model selection

Cloud deployment

##Author

Roshan S
Interests: Artificial Intelligence, Generative AI, Full Stack Development, MLOps

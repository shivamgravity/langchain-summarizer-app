# LangChain Text Summarizer API

This project implements a text summarization API using **FastAPI**, **LangChain**, and **Groq**. It demonstrates how to integrate Large Language Models (LLMs) into a standard RESTful API architecture.

## Project Overview

The goal of this project is to create a lightweight, high-performance API that leverages the power of LLMs to generate concise summaries of long text inputs.

**Key Features:**
* **FastAPI Backend:** A modern, high-performance web framework for building APIs with Python.
* **LangChain Integration:** Utilizes LangChain for prompt management and LLM interaction.
* **Groq Inference:** Powered by the ultra-fast Llama-3 model via the Groq API.
* **Swagger UI:** Automatic interactive API documentation for easy testing.

## Prerequisites

* **Python 3.10+**
* **Groq API Key** (Free tier available at console.groq.com)

## Setup & Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/shivamgravity/langchain-summarizer-app
    cd langchain-summarizer-app
    ```

2.  **Set Up Virtual Environment**
    ```bash
    # Create venv
    python -m venv venv

    # Activate venv (Windows)
    venv\Scripts\activate

    # Activate venv (Mac/Linux)
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**
    Create a `.env` file in the root directory and add your API key:
    ```text
    GROQ_API_KEY=gsk_your_key_here...
    ```

## How to Run

1.  **Start the Server:**
    Run the application using Uvicorn:
    ```bash
    python app.py
    ```
    *The server will start at `http://localhost:8000`*

2. **Go to >** `http://localhost:8000`and paste the text content in the box.

3. Click **Summmarize** to see the summary under 100 words.

## Solution Architecture

This project wraps an LLM chain in a REST API:

* **API Layer (FastAPI):** Handles incoming HTTP POST requests, validates the input using Pydantic models, and returns JSON responses.
* **Orchestration Layer (LangChain):**
    * **Prompt Template:** Defines the system instructions ("Summarize this text...").
    * **Chain:** Pipes the prompt into the LLM.
* **Inference Layer (Groq):** Executes the Llama-3 model to generate the summary text.

## API Reference

| Method | Endpoint | Description | Request Body | Response |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/summarize` | Summarizes input text | `{"text": "string"}` | `{"summary": "string"}` |

You can go to `http://localhost:8000/docs` to see the details of the API endpoints.
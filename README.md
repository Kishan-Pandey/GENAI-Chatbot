# QnA Chatbot with LangChain and OpenAI

This project is a **Streamlit-based chatbot** that answers user questions using OpenAI's language models and LangChain. It provides a simple UI for interacting with various LLMs and customizing settings like temperature and max tokens.

## Features

- Select from multiple OpenAI models (`gpt-4-turbo`, `gpt-4o`, `gpt-4`)
- Adjustable temperature and max tokens
- Secure API key input
- LangChain integration for prompt management and output parsing

## Setup

1. **Clone the repository**
git clone <your-repo-url>
cd GenAI_Project

2. **Install the requirements**

pip install -r requirements.txt

3. **Run the Streamlit app**

Open the provided local URL in your browser.  
Enter your OpenAI API key in the sidebar, select the desired model, adjust settings, and ask questions.

## File Structure

- `app.py`: Main Streamlit application
- `requirements.txt`: Python dependencies
- `.env`: Environment variables for API keys

## Dependencies

- streamlit
- langchain
- langchain_openai
- langchain_community
- langchain_core
- python-dotenv
- dotenv

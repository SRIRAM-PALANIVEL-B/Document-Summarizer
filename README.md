# Document-Summarizer


# Document Summarizer App

This project is a Document Summarizer application that allows users to upload text files or input text manually for summarization using OpenAI's GPT model. Built with Streamlit, it provides a user-friendly interface for analyzing and summarizing text documents.

## Features
- **File Upload**: Supports both `.txt` and `.docx` files for text extraction.
- **Manual Input**: Allows users to enter text directly into the application for analysis.
- **Text Preprocessing**: Cleans the text by removing punctuation, extra spaces, and non-alphanumeric characters.
- **Summarization**: Utilizes OpenAI's GPT model to generate concise summaries of the provided text.

## Technologies Used
- **Python**: The main programming language used for the application.
- **Streamlit**: Framework for building the web application interface.
- **OpenAI API**: For generating summaries using the GPT model.
- **docx2txt**: Library for extracting text from `.docx` files.
- **dotenv**: For managing environment variables securely.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/document-summarizer.git
   cd document-summarizer


# Create a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
# Install the required packages:

    pip install -r requirements.txt
    
# Create a .env file in the root directory and add your OpenAI API key:

    OPENAI_API_KEY=your_api_key_here
    
# Usage

To run the application, execute the following command:

    streamlit run app.py
    
Open your web browser and navigate to http://localhost:8501 to access the Document Summarizer App.

# How It Works

  - Users can upload a .txt or .docx file or enter text manually.
  - The application extracts the text from the uploaded file or uses the input text.
  - It preprocesses the text to clean it by removing unwanted characters and formatting.
  - The cleaned text is then sent to OpenAI's GPT model for summarization.
  - The summary is displayed on the application interface.
    
# Environment Variables

To use the OpenAI API, you need to set the following environment variable:

  - OPENAI_API_KEY: Your OpenAI API key.

Make sure to keep this key private and secure.





![Project Logo](logo.png)

import os
import re
import string

import docx2txt
import requests
import streamlit as st
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

# using OpenAI GPT to summarize text
def summarize_text(text):
    prompt = "Summarize the following text. Provide a concise summary based on the input text: " + text

    # Retrieve the API key
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("API key for OpenAI is not set.")

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
            "max_tokens": 4096,  # Set max_tokens according to your needs
        }
    )
    
    # Print the status code and response text for debugging
    print(f"OpenAI response status code: {response.status_code}")
    print(f"OpenAI response text: {response.text}")

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        if data.get("choices"):
            response_text = data["choices"][0]["message"]["content"]
        else:
            response_text = "No response from OpenAI."
    else:
        response_text = f"Error {response.status_code}: {response.text}"

    return response_text


# Create a directory to store uploaded files
def save_uploaded_file(uploaded_file):
    # Create 'uploads' directory if it doesn't exist
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    # Save the file
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path


# Process the uploaded file
def process_uploaded_file(uploaded_file):
    content = ""
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        content = docx2txt.process(uploaded_file)
    elif uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
    return content


# Clean the text for preprocessing
def clean_text(text):
    text = text.lower()
    text = " ".join(text.split())
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s.]", "", text)
    return text


# Main function
def main():
    st.title('Document Summarizer App')
    st.write('Upload a text file or enter text to analyze.')

    # Upload file or input text
    uploaded_file = st.file_uploader("Choose a file", type=['txt', 'docx'])
    text_input = st.text_area("Or enter text manually")

    # Initialize content variable
    content = None

    if uploaded_file is not None:
        # Process uploaded file
        file_path = save_uploaded_file(uploaded_file)
        content = process_uploaded_file(uploaded_file)
    elif text_input:
        # Use manually entered text
        content = text_input.strip()

    # Display the content
    if content:
        st.subheader('Original Content')
        st.text_area("Original Text", value=content, height=400)

        # Clean the content
        cleaned_content = clean_text(content)
        st.subheader('Preprocessed Content')
        st.text_area("Preprocessed Text", value=cleaned_content, height=400)

        # Check if cleaned content is sufficient
        if len(cleaned_content) < 10:
            st.warning('The text provided is too short to summarize.')
        else:
            summary = summarize_text(cleaned_content)
            st.subheader('Summary')
            st.text_area("Summarized Text", value=summary, height=300)
    else:
        st.warning('Please upload a file or enter text.')


if __name__ == "__main__":
    main()


# Multi-Functional Chatbot Web Application

## Overview

This project involves the development of a web application that integrates multiple chatbots and a sentiment analysis tool. The application provides users with a versatile platform to interact with different types of chatbots and analyze text sentiment. Built using Flask, OpenAI API, and Hugging Face Transformers, this application offers a seamless and interactive experience.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **OpenAI API**: Used for generating responses from chatbots.
- **Hugging Face Transformers**: Provides sentiment analysis functionality.
- **HTML/CSS**: For structuring and styling the web interface.
- **Python**: The primary programming language used for backend logic.

## Application Structure

### `app.py`
- **Purpose**: Core of the web application. Manages routes, handles user requests, and integrates functionalities.
- **Key Routes**:
  - `/`: Homepage with navigation to other chatbots and sentiment analysis.
  - `/friendly`: Interface for interacting with the Friendly Chatbot.
  - `/pdf`: Interface for the PDF Chatbot.
  - `/sentiment_analysis`: Interface for sentiment analysis.

### Chatbot Modules

- **FriendlyChatbot (`friendly_chatbot.py`)**:
  - Provides friendly and supportive responses using OpenAI’s GPT-4 model.
- **PDFChatbot (`pdf_chatbot.py`)**:
  - Handles PDF uploads, extracts text, and interacts using OpenAI’s GPT-4 model.
- **Sentiment Analysis (`sentiment.py`)**:
  - Analyzes the sentiment of user-provided text using Hugging Face’s pre-trained models.

### HTML Templates

- **`index.html`**: Homepage with links to chatbot interfaces.
- **`friendly_chatbot.html`**: Interface for the Friendly Chatbot.
- **`pdf_chatbot.html`**: Interface for the PDF Chatbot.
- **`sentiment.html`**: Interface for sentiment analysis.

### CSS Styles (`styles.css`)

- **General Styles**: Defines font, button styles, and form elements.
- **Page-Specific Styles**: Includes layout adjustments and background image configurations.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
   cd repositoryname

2. **Create a Virtual Environment**:
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Set Up Environment Variables:**
   Create a .env file in the root directory.
   Add your OpenAI API key:
     OPENAI_API_KEY=your_openai_api_key_here
5. **Run App.py:**
   python app.py

## Usage
  Homepage: Navigate to the homepage to choose between different chatbots and sentiment analysis tools.
  Friendly Chatbot: Interact with a friendly chatbot that provides supportive responses.
  PDF Chatbot: Upload a PDF, extract text, and interact with the chatbot based on the content.
  Sentiment Analysis: Analyze the sentiment of a given text and get the sentiment score and confidence.

## Project Files
  
  'app.py'
  This is the main file of the web application. It sets up the Flask app, defines routes, and integrates the chatbot and sentiment analysis functionalities.

  'friendly_chatbot.py'
  Contains the logic for the Friendly Chatbot, which uses OpenAI's GPT-4 model to generate friendly responses.

  'pdf_chatbot.py'
  Handles PDF uploads, extracts text from the PDF using PyPDF2, and sets up a retrieval-based chatbot using OpenAI's GPT-4 model and FAISS for vector storage and retrieval.

  'sentiment.py'
  Uses Hugging Face's Transformers to analyze the sentiment of user-provided text.

## HTML Templates

  'index.html': Homepage with navigation links to the different functionalities.
  'friendly_chatbot.html': Interface for the Friendly Chatbot.
  'pdf_chatbot.html': Interface for the PDF Chatbot.
  'sentiment.html': Interface for sentiment analysis.

## CSS Styles (styles.css)
  Contains styles for the entire application, including general styles and page-specific adjustments.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Acknowledgements:
  I'd like to thank Mr. Usman Afridi for his efforts and teaching us the practical Implementations of various tools.

from flask import Flask, render_template, request, redirect, url_for
from friendly_chatbot import FriendlyChatbot
from pdf_chatbot import PDFChatbot
from sentiment import analyze_sentiment  # Import the function from sentiment.py

app = Flask(__name__)

# Initialize chatbots
friendly_chatbot = FriendlyChatbot()
pdf_chatbot = PDFChatbot(api_key="Input you API key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/friendly', methods=['GET', 'POST'])
def friendly():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = friendly_chatbot.get_response(user_input)
        return render_template('friendly_chatbot.html', user_input=user_input, response=response)
    return render_template('friendly_chatbot.html')

@app.route('/pdf', methods=['GET', 'POST'])
def pdf_chatbot_view():
    if request.method == 'POST':
        pdf_file = request.files.get('pdf_file')
        user_input = request.form.get('user_input')

        if pdf_file:
            pdf_file_path = f"uploaded_{pdf_file.filename}"
            pdf_file.save(pdf_file_path)
            pdf_chatbot.extract_text_from_pdf(pdf_file_path)

        response = pdf_chatbot.get_response(user_input)
        return render_template('pdf_chatbot.html', user_input=user_input, response=response)
    return render_template('pdf_chatbot.html')

@app.route('/sentiment_analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    sentiment = None
    confidence = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment, confidence = analyze_sentiment(text)
    return render_template('sentiment.html', sentiment=sentiment, confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)

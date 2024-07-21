from transformers import pipeline

# Initialize the sentiment analysis pipeline with the selected model
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    # Perform sentiment analysis on the provided text
    result = sentiment_analyzer(text)[0]
    sentiment = result['label']
    confidence = result['score']
    return sentiment, confidence

if __name__ == "__main__":
    # Example usage
    text = "I love using Hugging Face models!"
    sentiment, confidence = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")
    print(f"Confidence: {confidence:.2f}")

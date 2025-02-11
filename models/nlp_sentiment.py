from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    return sentiment_pipeline(text)[0]["label"]

if __name__ == "__main__":
    print(analyze_sentiment("I love this product!"))  # Output: Positive

# Libraries needed for environment variables, HTTP requests, and loading secret keys.
# os: access environment variables
# requests: make HTTP calls to the API
# load_dotenv: load secret keys from .env file

import os
import requests
from dotenv import load_dotenv

# First line loads the .env file. Second line fetches the file and stores the secret API token from .env file (excluded from GitHub via .gitignore).
load_dotenv()
api_token = os.getenv("HF_TOKEN")

# Hugging Face Inference API endpoint for DistilBERT sentiment analysis model.
API_URL = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

# Authentication headers sent with every API request to verify identity.
headers = {
    "Authorization" : "Bearer " + api_token
}

def analyze_sentiment(text):
    """
    This function analyzes the sentiment of text using the HF API.
    
    - text: the input we want to analyze
    - payload: packages the text into a format HF understands
    - requests.post: sends the package to HF along with our headers
    - response: where the result from HF lands after analysis
    """
    payload = {
        "inputs" : text
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()

result = analyze_sentiment(input("Enter a statement to analyze: "))
print("Sentiment: " + result[0][0]["label"])
print("Confidence: " + str(round(result[0][0]["score"] * 100, 2)) + "%")
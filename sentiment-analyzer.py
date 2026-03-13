import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization" : "Bearer " + api_token
}
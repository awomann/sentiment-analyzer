# Sentiment Analyzer

A Python application that analyzes the sentiment of any text using the Hugging Face Inference API. Type a sentence and the app returns whether the sentiment is Very Positive, Positive, Neutral, Negative, or Very Negative — along with a confidence score.

The app was originally built with DistilBERT as the baseline model, then upgraded to `tabularisai/robust-sentiment-analysis` for more nuanced 5-category output.

## Features

Here's what it can do:
* Accept user input directly from the terminal
* Send text to the Hugging Face API and receive a sentiment result
* Display the sentiment label and confidence score in a readable format
* Swap between sentiment models by updating a single URL

## Python Concepts Used

| Concept | What It Does |
|--------|-------------|
| **Imports** | Pulls in external libraries so the code can use their tools |
| **Environment Variables** | Stores the API token securely outside the codebase using a `.env` file |
| **Dictionaries** | Packages text into the format the API expects and parses the response |
| **Functions** | Wraps the API call into a reusable block that takes text and returns a result |
| **String Formatting** | Converts the raw API response into clean, human-readable output |
| **HTTP POST Requests** | Sends text to Hugging Face's servers using the `requests` library |

## Security
* The API token is stored in a `.env` file which is excluded from version control via `.gitignore`
* Never commit your `.env` file or paste your token directly in your code
* Generate a free token at [huggingface.co/settings/access-tokens](https://huggingface.co/settings/access-tokens) with **"Make calls to Inference Providers"** permission enabled

## How to Run

Use Python 3 with Miniconda recommended. Install dependencies first:

```
pip install requests python-dotenv
```

Add your Hugging Face token to a `.env` file in the project folder:

```
HF_TOKEN=your_token_here
```

Then run the program in your editor of choice. It will prompt you to enter a sentence and return the sentiment result immediately.

# Reaching into the transformers library and pulling out one specific tool called pipeline; installed the transformer library via the terminal using pip install transformers. The library is from the Hugging Face libraries.
from transformers import pipeline 

# Calling that pipeline tool and telling it "I want to do sentiment analysis." Behind the scenes it goes out and downloads a pre-trained model that already knows how to analyze sentiment. Then it packages everything up and stores it in your classifier variable, ready to use.
classifier = pipeline("sentiment-analysis")

result = classifier("I hate traveling.")
print(result)
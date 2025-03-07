from flask import Flask, render_template, request
from flask_cors import CORS
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
from sentiment_analysis import clean_text, load_csv

app = Flask(__name__)
CORS(app)

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

client = InferenceClient(
    "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    api_key=os.getenv("HUGGINGFACE_TOKEN")
)

@app.route('/predict', methods=['POST'])
def index():
    try:
        sentiment = None
        avis = request.args.get('avis')

        if avis.strip():
            result = client.text_classification(avis)
            sentiment = result[0]['label']
        return sentiment
    
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return {"error": "Internal Server Error"}, 500
    
@app.route('/trend', methods=['GET'])
def trend():
    df = load_csv()
    # Columns: "rate", "Reviews", "tokenized_reviews", "review_date", "Sentiment"
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)

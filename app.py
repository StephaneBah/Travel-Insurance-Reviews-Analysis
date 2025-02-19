from flask import Flask, render_template, request
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

client = InferenceClient(
    "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    api_key=os.getenv("HUGGINGFACE_TOKEN")
)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    avis = ""
    
    if request.method == 'POST':
        avis = request.form['avis']
        if avis.strip():
            result = client.text_classification(avis)
            sentiment = result[0]['label']

    return render_template('index.html', avis=avis, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

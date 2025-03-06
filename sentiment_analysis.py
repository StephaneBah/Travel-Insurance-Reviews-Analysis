import pandas as pd
import numpy as np
import emoji
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def clean_text(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Décodage des emojis
    text = emoji.demojize(text, delimiters=("", ""))  # Remplace les emojis par leur description textuelle
    # Gestion des répétitions
    text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)  # Supprime les mots répétés consécutifs
    # Conversion en minuscules
    text = text.lower()
    # Suppression de la ponctuation et des chiffres
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Suppression des stop words et lemmatisation
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])
    return text

def load_csv():
    df = pd.read_csv('NLP/Travel-Insured-International_Custumers_Reviews-after_preprocessing.csv')
    return df


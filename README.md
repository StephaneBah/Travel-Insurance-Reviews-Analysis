# Travel-Insurance-Reviews-Analysis

## Détection de Sentiment avec Flask et HuggingFace API

Ce projet est une application Flask permettant d’analyser le sentiment d’un texte saisi par l’utilisateur,
en utilisant le modèle DistilBERT via l’API HuggingFace.

### 1. Cloner le dépôt

```bash
git clone https://github.com/StephaneBah/Travel-Insurance-Reviews-Analysis.git
cd Travel-Insurance-Reviews-Analysis
```

### 2. Créer un environnement virtuel

```bash
python 3.12.4
```
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Installation des dépendances

```bash
pip install -r requirements.txt
```
```bash
python nltk_download.py
```
### 4. Configuration de l'API HuggingFace

Créez un compte sur [HuggingFace](https://huggingface.co)
Générez un jeton d'API [ici](https://huggingface.co/settings/tokens)
Créez un fichier `.env` à la racine du projet et ajoutez la ligne suivante :
```properties
HUGGINGFACE_TOKEN = votre_jeton_huggingface
```

### 5. Lancer l'Application

```bash
python app.py
```

### 6. Accéder aux endpoints

[http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict)

[http://127.0.0.1:5000/trend](http://127.0.0.1:5000/trend)


## Configuration pour le front end dans le dossier Frontend

NB: Ouvrir un autre terminal en parallèle
```
cd Frontend
```
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your unit tests
```
npm run test:unit
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Actualisation des avis(Non Recommandé- La structure du site scrapé à changer récemment) 
Pour actualiser les avis, il faut exécuter le notebook Scraping.ipynb puis Preprocessing.ipynb (du dossier **NLP**) en s'assurant avoir installer tous les packages et modules du requirements.txt et nltk_download.py. S'assurer aussi de copier dans le dossier NLP le fichier .env contenant la clé API Hugging Face. 
NB: Dans la prochaine version nous allons essayer d'automatiser tout le processus.

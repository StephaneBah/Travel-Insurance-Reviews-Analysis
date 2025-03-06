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

### 6. Accéder à l'application

[http://127.0.0.1:5000](http://127.0.0.1:5000)

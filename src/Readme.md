# Puls Events – RAG Chatbot Data Engineering Project

## Présentation

Puls-Events est un projet de chatbot intelligent basé sur une architecture RAG (Retrieval-Augmented Generation) permettant d'interroger des événements publics en Île-de-France à partir de données Open Data.

**Le système :**

ingère des données publiques via API

les transforme et nettoie

les indexe via FAISS

permet une recherche sémantique

génère des réponses contextualisées avec un LLM (Mistral)

**Objectifs du projet**

Construire un pipeline data complet (ingestion → vectorisation → exploitation)

Mettre en place une architecture RAG moderne

Appliquer des bonnes pratiques Data Engineering

Intégrer des tests de validation des données

---

## Architecture du projet

**la structure du projet se présente comme suite :** 

puls-events-rag/
│
├── README.md
├── requirements.txt
├── .env.example
│
├── data/
│   ├── events.csv
│   └── faiss_index/
│
├── src/
│   ├── ingest.py
│   ├── vectorize.py
│   └── chat.py
│
├── tests/
│   └── test_events.py
│
└── run.py

![Diagramme des flux](./image.png)

---

## Description des fichiers

**src/ingest.py :** 
- Récupère les événements via API OpenDataSoft

- Filtre les événements d’Île-de-France

- Sauvegarde en data/events.csv

**src/vectorize.py:**

- Transforme les données en documents texte

- Génère les embeddings via Mistral

- Crée un index FAISS local

**src/chatbot.py:**

- Charge l’index FAISS

- Interroge le retriever

- Construit un prompt RAG

- Génère une réponse via Mistral

**tests/test_events.py:**

- vérifie si les événements ont moins d’un an

- vérifie s’ils ont bien lieu en Île-de-France

---

## Installation

1️⃣ Cloner le projet
git clone <repo_url>
cd puls-events-rag

2️⃣ Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Installer les dépendances
pip install -r requirements.txt

4️⃣ Configurer les variables d’environnement

Créer un fichier .env :

MISTRAL_API_KEY=your_api_key_here

▶️ **Lancer le projet** 

1️⃣ Ingestion
python src/ingest.py

2️⃣ Vectorisation
python src/vectorize.py

3️⃣ Tests
python -m pytest

4️⃣ Chat
python src/chat.py

▶️ **Lancer tous le projet** : **python run.py**

---

## Stack technique

- Python

- Pandas

- FAISS

- LangChain

- Mistral API

- Pytest

- dotenv

---

## Améliorations futures

- Filtrage temporel intelligent

- Déploiement API (FastAPI)

- Dockerisation

- CI/CD

- Monitoring des performances

- Ajout de métadonnées dans FAISS

# 👤 Owner

<h1 align="center">Hi 👋, I'm khalid</h1>
<h3 align="center"> Data & Cloud Engineer|| Power BI and Qlik sense developer</h3>

Ce projet a été réalisé par :

**khalid OURO-ADOYI**  

📧 Email : khalidouroadoyi@gmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/khalid-ouro-adoyi/) | [GitHub](https://github.com/LIDONI)
- 📫 How to reach me **khalidouroadoyi@gmail.com**

- 👨‍💻 All of my projects are available at [https://github.com/lidoni?tab=repositories](https://github.com/lidoni?tab=repositories)

- 📄You can see my presentations in my linkedin posts [https://www.linkedin.com/in/khalid-ouro-adoyi/](https://www.linkedin.com/in/khalid-ouro-adoyi/)

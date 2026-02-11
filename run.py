# Script principal pour lancer le POC complet
import os
from src.ingest import fetch_events
from src.vectorize import build_index
from src.chat import poser_question

if __name__ == "__main__":
    #  Ingestion des événements
    print("Récupération des événements...")
    fetch_events()

    #  Création de l'index FAISS
    print("Création de l'index FAISS...")
    build_index()

    #  Lancer le chatbot
    print("Lancement du chatbot Puls-Bot...")
    poser_question("Quels événements culturels sont prévus prochainement en Île-de-France ?")

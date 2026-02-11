import os
import pandas as pd
from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

def build_index():
    df = pd.read_csv("data/events.csv")

    docs = []
    for _, r in df.iterrows():
        text = f"TITRE: {r.title}\nLIEU: {r.location_name} à {r.location_city}\nDATE: {r.firstdate_begin}\nDESCRIPTION: {r.description}"
        docs.append(Document(
            page_content=text,
            metadata={
                "title": r.title,
                "city": r.location_city,
                "date": r.firstdate_begin,
                "region": r.location_region,
                "location_name": r.location_name
            }
        ))

    embeddings = MistralAIEmbeddings(mistral_api_key=API_KEY)
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("data/faiss_index")
    print(f"✅ Index FAISS créé avec {len(docs)} documents.")

if __name__ == "__main__":
    build_index()

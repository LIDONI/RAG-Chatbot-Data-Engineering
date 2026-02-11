import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS

# Charger les variables d'environnement
load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")
if not API_KEY:
    raise ValueError("MISTRAL_API_KEY non trouvé dans le fichier .env")

# Initialiser les embeddings
embeddings = MistralAIEmbeddings(mistral_api_key=API_KEY)

# Charger l'index FAISS en autorisant la désérialisation
vector_db = FAISS.load_local(
    "data/faiss_index",
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})


# Initialiser le modèle LLM Mistral
llm = ChatMistralAI(model="mistral-medium", mistral_api_key=API_KEY)

# Prompt RAG
PROMPT = PromptTemplate(
    template="""
Tu es l'assistant intelligent de Puls-Events.
Utilise UNIQUEMENT les éléments de contexte suivants pour répondre à la question.
Si tu ne sais pas, dis-le clairement sans inventer.
Réponds en français, de manière cordiale, avec les infos pratiques (lieu, date).

Contexte :
{context}

Question :
{question}

Réponse :
""",
    input_variables=["context", "question"]
)

def poser_question(question: str):
    docs = retriever._get_relevant_documents(question,run_manager=None)
    context = "\n".join([d.page_content for d in docs])
    prompt_text = PROMPT.format(context=context, question=question)
    result = llm.invoke(prompt_text)
    print(f"\nQuestion : {question}\nPuls-Bot : {result}\n")
    return result

# Exemple interactif
if __name__ == "__main__":
    while True:
        q = input("Pose ta question > ")
        if q.lower() in ["exit", "quit"]:
            break
        poser_question(q)

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Legal RAG Chatbot", layout="wide")
st.title("📄 Legal Docs Q&A Chatbot (RAG Powered)")

# File upload
uploaded_file = st.file_uploader("Upload a legal document (.txt)", type=["txt"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp_doc.txt", "w", encoding="utf-8") as f:
        f.write(uploaded_file.read().decode())

    # Load and split document
    loader = TextLoader("temp_doc.txt")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    # Embeddings & Vector store
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()

    # QA chain
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Question input
    user_question = st.text_input("Ask a question about the document:")
    if user_question:
        with st.spinner("Generating answer..."):
            result = qa.run(user_question)
            st.success(result)

from transformers import pipeline

# Add any additional setup code here if needed
import torch
import PyPDF2 # pdf reader
import time
from pypdf import PdfReader
from io import BytesIO
from langchain.prompts import PromptTemplate # for custom prompt specification
from langchain.text_splitter import RecursiveCharacterTextSplitter # splitter for chunks
from langchain.embeddings import HuggingFaceEmbeddings # embeddings
from langchain.vectorstores import FAISS # vector store database
from langchain.chains import RetrievalQA # qa and retriever chain
from langchain.memory import ConversationBufferMemory # for model's memoy on past conversations
from langchain.document_loaders import PyPDFDirectoryLoader # loader fo files from firectory

# Define a sample command
def main():
    print("Hello from the Hugging Face Spaces app!")

# Run the main command if the file is executed
if __name__ == "__main__":
    main()

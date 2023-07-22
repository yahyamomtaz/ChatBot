import langchain
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone 
from langchain.vectorstores import Pinecone
from langchain.embeddings import SentenceTransformerEmbeddings

directory = 'data'

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)

def split_docs(documents,chunk_size=500,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)


embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# initialize pinecone
pinecone.init(
    api_key="7097682e-9631-4b87-98fa-704c5ea7097f",  # find at app.pinecone.io
    environment="us-west4-gcp-free"  # next to api key in console
)

index = pinecone.Index('law-agent')

index = Pinecone.from_documents(docs, embeddings, index_name=index)
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# Set up API keys
openai_api_key = os.environ.get("OPENAI_API_KEY")
pinecone_api_key = os.environ.get("PINECONE_API_KEY")
pincone_index_name = os.environ.get("PINECONE_INDEX_NAME")

def get_openai_llm(model='gpt-3.5-turbo', temperature=0):
  llm = ChatOpenAI(
    model_name=model,
    temperature=temperature,
    openai_api_key=openai_api_key
  )
  return llm

def get_openai_embedding():
  embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
  return embedding

def get_pinecone_vectorstore():
  index_name = pincone_index_name
  embedding = get_openai_embedding()
  vectorstore = PineconeVectorStore(index_name=index_name, embedding=embedding)
  return vectorstore
  
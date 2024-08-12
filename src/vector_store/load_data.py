import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

# Load environment variables from the .env file
load_dotenv()

def create_vectorstore():
    """
    Create a vector store using movie history documents.

    This function loads the movie history documents from a specified text file,
    splits the documents into chunks, initializes the OpenAI embeddings, and connects
    to Pinecone to create or access a vector store.

    The environment variables OPENAI_API_KEY, PINECONE_API_KEY, and PINECONE_INDEX
    must be set for the function to operate correctly.

    Raises:
        Exception: If there is an issue with loading documents or connecting to Pinecone.
    """
    
    # Define the path to movie_history.txt
    movie_history_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'movie_history.txt')

    # Load the documents
    loader = TextLoader(movie_history_path)  
    documents = loader.load()  
    
    # Split the loaded documents into smaller chunks for processing
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  
    docs = text_splitter.split_documents(documents)  

    # Retrieve API keys and index name from environment variables
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    pinecone_api_key = os.environ.get("PINECONE_API_KEY")
    pinecone_index_name = os.environ.get("PINECONE_INDEX_NAME")

    # Initialize OpenAI embeddings and Pinecone
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    pc = Pinecone(api_key=pinecone_api_key)

    # Create or connect to the Pinecone index
    index_name = pinecone_index_name
    if index_name not in pc.list_indexes().names():  
        print(f"pinecone {index_name} is not exist, create index and try again")
        return

    print("Vector is storing, wait...")
    # Create the vector store using the split documents and embeddings
    vectorstore = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)
    print("Vector store created successfully!") 

if __name__ == "__main__":
    create_vectorstore()  

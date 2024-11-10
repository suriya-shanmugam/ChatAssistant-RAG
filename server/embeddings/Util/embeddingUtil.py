from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma"

# Ensure your  API key is configured

def get_embedding_function() :
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return embedding



def fetch_relevant_chunks(query,docpath):
    
    # Initialize embeddings model
    embedding_model = get_embedding_function() 

    # Load the Chroma vectorstore
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH+'/'+docpath,
        embedding_function=embedding_model
    )

    # Perform a similarity search in ChromaDB with the query
    relevant_chunks = vectorstore.similarity_search(query, k=5)

    return relevant_chunks

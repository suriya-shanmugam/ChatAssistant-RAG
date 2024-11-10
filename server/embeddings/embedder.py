import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma


import Util.embeddingUtil

PDF_DOCS_PATH = "docs"
CHROMA_PATH = "chroma"


def store_embeddings_in_chromadb(pdf_path, doc_name="doc1"):
    
    # Load the PDF document
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split the document into chunks (adjust chunk size as needed)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_documents = text_splitter.split_documents(documents)

    # Generate embeddings using OpenAI embeddings (ensure your API key is set)
    embedding_model = Util.embeddingUtil.get_embedding_function()

    # Create and store embeddings in ChromaDB for this specific document
    vectorstore = Chroma.from_documents(
        documents=split_documents,
        embedding=embedding_model,
        persist_directory=os.path.join(CHROMA_PATH, doc_name)  # Separate vector store for each document
    )

    # Persist the vector store on disk
    vectorstore.persist()

    print(f"Embeddings for {doc_name} stored successfully in ChromaDB!")


if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)


pdf_path_doc1 = "docs/1.pdf"  
pdf_path_doc2 = "docs/2.pdf"
store_embeddings_in_chromadb(pdf_path_doc1, doc_name="doc1")
store_embeddings_in_chromadb(pdf_path_doc2, doc_name="doc2")
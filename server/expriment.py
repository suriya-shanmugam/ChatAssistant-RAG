import os
import shutil

from langchain_community.document_loaders import PyPDFLoader

PDF_DOCS_PATH = "docs"
CHROMA_PATH = "chroma"

all_documents = []

    # Iterate over each file in the directory
for filename in os.listdir(PDF_DOCS_PATH):
        # Check if the file is a PDF
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(PDF_DOCS_PATH, filename)
        # Load the PDF file using PyPDFLoader
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        all_documents.extend(documents)

print(len(all_documents))        
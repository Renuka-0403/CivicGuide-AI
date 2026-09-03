from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# --------------------------------------------------
# 1. Locate government PDF folder
# --------------------------------------------------

DATA_FOLDER = Path("Government_Data")
VECTOR_DB_FOLDER = Path("vector_db")


# --------------------------------------------------
# 2. Find all PDF files
# --------------------------------------------------

pdf_files = list(DATA_FOLDER.rglob("*.pdf"))

print(f"\nFound {len(pdf_files)} PDF files.")

if not pdf_files:
    print("ERROR: No PDF files found.")
    print("Check that your PDFs are inside Government_Data.")
    exit()


# --------------------------------------------------
# 3. Read all PDFs
# --------------------------------------------------

all_documents = []

for pdf_file in pdf_files:

    print(f"\nReading: {pdf_file.name}")

    try:
        loader = PyPDFLoader(str(pdf_file))
        documents = loader.load()

        # Add useful information to metadata
        for document in documents:
            document.metadata["source_file"] = pdf_file.name

            if "TamilNadu" in str(pdf_file):
                document.metadata["government"] = "Tamil Nadu Government"
            elif "Central_Government" in str(pdf_file):
                document.metadata["government"] = "Central Government"

        all_documents.extend(documents)

        print(f"  Pages loaded: {len(documents)}")

    except Exception as e:
        print(f"  ERROR reading {pdf_file.name}: {e}")


print(f"\nTotal pages loaded: {len(all_documents)}")


# --------------------------------------------------
# 4. Split documents into smaller chunks
# --------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

chunks = text_splitter.split_documents(all_documents)

print(f"Total text chunks created: {len(chunks)}")


# --------------------------------------------------
# 5. Create embeddings
# --------------------------------------------------

print("\nLoading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

print("Embedding model loaded.")


# --------------------------------------------------
# 6. Create FAISS vector database
# --------------------------------------------------

print("\nCreating FAISS vector database...")

vector_db = FAISS.from_documents(
    chunks,
    embeddings
)


# --------------------------------------------------
# 7. Save vector database
# --------------------------------------------------

VECTOR_DB_FOLDER.mkdir(exist_ok=True)

vector_db.save_local(str(VECTOR_DB_FOLDER))

print("\n======================================")
print("CIVICGUIDE AI KNOWLEDGE BASE READY!")
print("======================================")
print(f"PDF files: {len(pdf_files)}")
print(f"Pages: {len(all_documents)}")
print(f"Text chunks: {len(chunks)}")
print(f"Vector database: {VECTOR_DB_FOLDER}")
print("======================================")
# 🏛️ CivicGuide AI

### RAG-Powered Personalized Government Scheme & Service Assistant

**Team:** QuadraMind 🧠  
**Tagline:** *Four Minds. One Innovation.*

> **Making Government Services Simple, Accessible, and Intelligent.**

---

## 📌 Project Overview

CivicGuide AI is a **Retrieval-Augmented Generation (RAG)** based AI assistant designed to help citizens understand government welfare schemes and services through natural-language interaction.

Government scheme information is often distributed across multiple websites and lengthy official documents. Eligibility conditions, required documents, benefits, and procedures can also be difficult to understand.

CivicGuide AI addresses this challenge by retrieving relevant information from a knowledge base of **official Central Government and Tamil Nadu Government documents** and using a Large Language Model to generate clear, context-based responses.

The system combines **RAG, FAISS vector retrieval, Sentence Transformers, LangChain, and Groq-powered LLM generation** to provide source-grounded information.

---

## 🎯 Problem Statement

Citizens may face several difficulties when trying to access government welfare scheme information:

- Information is distributed across multiple websites and documents.
- Eligibility conditions can be detailed and difficult to interpret.
- Different schemes require different documents.
- Citizens may not know which scheme is relevant to their situation.
- Official government documents may contain complex administrative terminology.
- Manually searching lengthy PDF guidelines can be time-consuming.

CivicGuide AI aims to make this information easier to find and understand through an intelligent natural-language interface.

---

## 💡 Proposed Solution

CivicGuide AI uses a **Retrieval-Augmented Generation (RAG)** approach.

Instead of relying entirely on the LLM's pre-trained knowledge, the system first retrieves relevant information from official government documents and then provides the retrieved context to the LLM.

The system can generate responses related to:

- Government scheme information
- Eligibility-related conditions
- Benefits
- Required documents
- Relevant government departments
- Other scheme-related information available in the knowledge base

The responses are grounded in the retrieved official documents to reduce unsupported or fabricated information.

---

## ✨ Key Features

### 👤 Personalized Profile

Users can provide relevant information such as:

- Age
- Gender
- State and District
- Education details
- Family income
- Occupation
- Worker type
- Welfare board registration details
- Special circumstances
- Other eligibility-related information

These details are used as contextual information when processing queries.

### 🔎 RAG-Based Retrieval

The system retrieves relevant information from indexed official government documents before generating a response.

### 🤖 AI-Powered Responses

The retrieved information is provided to an LLM through the **Groq API**, which generates clear and natural-language responses.

### 📄 Official Document Knowledge Base

The knowledge base contains government scheme documents from:

- Government of India
- Government of Tamil Nadu

### 🛡️ Source-Grounded Answers

The application provides source evidence from the retrieved documents to make responses more transparent and reliable.

### 🚫 Anti-Hallucination Handling

If sufficient information cannot be found in the available official documents, the system avoids guessing and informs the user that additional official information is required.

### 🌐 Web-Based Interface

The application is built using Streamlit and deployed online for easy access.

---

## 🏗️ System Architecture

```text
                    CIVICGUIDE AI
                         │
                         ▼
             ┌─────────────────────┐
             │ Official Government  │
             │       PDFs           │
             └──────────┬──────────┘
                        │
                        ▼
                  PyPDF Extraction
                        │
                        ▼
                 LangChain Chunking
                        │
                        ▼
             Sentence Transformers
                  Embeddings
                        │
                        ▼
               FAISS Vector Database
                        │
                        │
        ┌───────────────┘
        │
        ▼
   User Profile + Question
        │
        ▼
   Query Processing
        │
        ▼
    FAISS Retrieval
        │
        ▼
 Relevant Government Information
        │
        ▼
      RAG Context
        │
        ▼
 Groq API + GPT-OSS-120B
        │
        ▼
 Personalized Response
        │
        ▼
   Source Evidence
 

### 🔄 How It Works
1. Knowledge Preparation

Official government PDF documents are processed and converted into a searchable knowledge base.

Government PDFs
      ↓
PyPDF Text Extraction
      ↓
LangChain Text Chunking
      ↓
Sentence Transformers Embeddings
      ↓
FAISS Vector Database
2. Question Answering

When a user submits their profile information and a question, the system retrieves relevant information and generates a response.

User Profile + Question
          ↓
    Query Processing
          ↓
     FAISS Retrieval
          ↓
Relevant Government Information
          ↓
       RAG Context
          ↓
Groq API + GPT-OSS-120B
          ↓
  Personalized Response
          ↓
     Source Evidence
3. RAG Concept

CivicGuide AI follows the standard Retrieval-Augmented Generation pipeline:

INPUT
  ↓
RETRIEVE
  ↓
AUGMENT
  ↓
GENERATE
  ↓
SOURCE-BACKED OUTPUT


### 🛠️ Technologies Used

Programming & Interface
Technology	Purpose
Python	Core programming language
Streamlit	Interactive web application interface
VS Code	Development environment
Generative AI
Technology	Purpose
Groq API	Provides access to the Large Language Model
GPT-OSS-120B	Large Language Model used for response generation through Groq
RAG Pipeline
Technology	Purpose
LangChain	Document processing and RAG orchestration
PyPDF	Extracts text from government PDF documents
Sentence Transformers	Converts text into vector embeddings
all-MiniLM-L6-v2	Embedding model used for semantic search
FAISS	Stores and retrieves relevant document chunks
Configuration & Deployment
Technology	Purpose
python-dotenv	Loads environment configuration
GitHub	Source code management
Streamlit Community Cloud	Application deployment


### 📚 Knowledge Base

CivicGuide AI uses official government documents as its primary knowledge source.

### 🇮🇳 Central Government

The knowledge base includes documents related to schemes such as:

PM Vishwakarma
PM-KISAN
National Scholarship Portal
Other available Central Government scheme documents

### 🏛️ Tamil Nadu Government

The knowledge base includes documents related to schemes such as:

Pudhumai Penn
Tamil Pudhalvan
Tamil Nadu Labour Welfare Board Educational Assistance
Other available Tamil Nadu Government scheme documents

The system provides information based on the official documents available in its knowledge base.

### 🧪 Testing & Test Cases

The application was tested using different types of government scheme-related queries to verify retrieval and response generation.

Test Case 1 – Tamil Nadu Labour Welfare Board Educational Assistance

Query:

Explain the Tamil Nadu Labour Welfare Board Educational Assistance scheme and tell me what information and documents are needed to determine eligibility.

Expected Result:

Retrieve relevant scheme information, eligibility-related details, and required documents from the available official documents.

Result: ✅ Pass

Test Case 2 – PM Vishwakarma

Query:

What is the PM Vishwakarma scheme, who is eligible for it, what benefits are provided, and what documents are required?

Expected Result:

Provide scheme details, eligibility conditions, benefits, and required documents based on the retrieved official documents.

Result: ✅ Pass

Test Case 3 – Pudhumai Penn

Query:

Which government department is responsible for the Pudhumai Penn scheme?

Expected Result:

Identify the responsible government department using the available official information.

Result: ✅ Pass


### 🚀 Deployment

CivicGuide AI has been successfully deployed using Streamlit Community Cloud.

### 🌐 Live Application

CivicGuide AI – Live Demo:
https://civicguide-ai-cojbj9ndsvi8rtiemia7fz.streamlit.app/

### 🔐 API Key Security

The Groq API key is stored securely using environment variables during local development and Streamlit Secrets during deployment.

The API key is not included in the source code or GitHub repository.

### ⚠️ Limitations

The system can only provide information available in its current government-document knowledge base.
It does not replace official government verification.
Eligibility assessment is based on the official documents provided to the system.
Final eligibility decisions are made by the concerned government authority.
Government schemes and guidelines may change over time, requiring the knowledge base to be updated.
The system does not directly submit applications to government portals.
The accuracy of responses depends on the quality and completeness of the available official documents.

###🔮 Future Enhancements

Future versions of CivicGuide AI could include:

🌐 Integration with more government schemes and departments
🗣️ Tamil and multilingual support
📱 Mobile-friendly interface
🔄 Automatic updating of government documents
🔗 Direct links to official application portals
📋 Step-by-step application guidance
🧠 Improved eligibility assessment
🔔 Scheme update and deadline notifications
🎙️ Voice-based interaction
📊 Advanced personalized scheme recommendations
🎓 Project Outcome

CivicGuide AI demonstrates the practical application of Generative AI and Retrieval-Augmented Generation to a real-world public-service problem.

The project combines document processing, semantic search, vector retrieval, Large Language Models, and a web interface to make government scheme information easier to access and understand.

The successful deployment demonstrates an end-to-end AI application:

Official Government Documents
            ↓
     Document Processing
            ↓
     Vector Embeddings
            ↓
       FAISS Retrieval
            ↓
         RAG Context
            ↓
          Groq LLM
            ↓
   Personalized Response
            ↓
      Source Evidence

### 📖 References
Government Sources
Government of India – National Scholarship Portal
Government of India – PM Vishwakarma
Government of India – PM-KISAN
Tamil Nadu Government – Tamil Nadu Integrated Learning and Schemes
Tamil Nadu Social Welfare and Women Empowerment Department
Tamil Nadu Labour Welfare Board
Tamil Nadu Unorganised Workers Welfare Board
Technology Documentation
Python
Streamlit
LangChain
FAISS
Hugging Face Sentence Transformers
Groq API

### 📄 Disclaimer

CivicGuide AI is an educational and informational AI project.

The information provided by the application is based on the official government documents available in its knowledge base. The application does not represent or act on behalf of any government department.

Eligibility assessments are informational and based on the official documents available to the system. Final eligibility and approval are determined by the concerned government authority.

### ⭐ CivicGuide AI
Making Government Services Simple, Accessible, and Intelligent.

Built with Python • RAG • FAISS • LangChain • Hugging Face • Groq • Streamlit

Team QuadraMind 🧠 — Four Minds. One Innovation.



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

The application is built using **Streamlit** and deployed online for easy access.

---

## 🏗️ System Architecture

```text
                         CIVICGUIDE AI
                              │
                              ▼
                  ┌────────────────────────┐
                  │ Official Government PDFs│
                  └────────────┬───────────┘
                               │
                               ▼
                       PyPDF Text Extraction
                               │
                               ▼
                      LangChain Text Chunking
                               │
                               ▼
                   Sentence Transformers
                         Embeddings
                               │
                               ▼
                      FAISS Vector Database
                               │
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

---
### 1. Knowledge Preparation

Official government PDF documents are processed and converted into a searchable knowledge base.

```text
Government PDFs
      ↓
PyPDF Text Extraction
      ↓
LangChain Text Chunking
      ↓
Sentence Transformers Embeddings
      ↓
FAISS Vector Database
```

---

## ❓ Question Answering

CivicGuide AI allows users to ask natural-language questions about government schemes and services.

Users can ask questions such as:

- What is the eligibility for a particular government scheme?
- What benefits are provided by the scheme?
- What documents are required?
- Which government department manages the scheme?
- What information is needed to assess eligibility?
- Which schemes may be relevant based on the user's profile?

The system processes the user's profile and question, retrieves relevant information from the official government knowledge base, and generates a clear response using the Groq-powered LLM.

If sufficient information is not available in the retrieved documents, the system avoids guessing and informs the user that additional official information is required.

### 3. RAG Concept

CivicGuide AI follows the **Retrieval-Augmented Generation (RAG)** pipeline:

```text
INPUT
  ↓
RETRIEVE
  ↓
AUGMENT
  ↓
GENERATE
  ↓
SOURCE-BACKED OUTPUT
```

---

## 📚 Knowledge Base

CivicGuide AI uses **official government documents** as its primary knowledge source.

### 🇮🇳 Central Government

The knowledge base includes documents related to schemes such as:

- **PM Vishwakarma**
- **PM-KISAN**
- **National Scholarship Portal (NSP)**
- **Other available Central Government scheme documents**

### 🏛️ Tamil Nadu Government

The knowledge base includes documents related to schemes such as:

- **Pudhumai Penn**
- **Tamil Pudhalvan**
- **Tamil Nadu Labour Welfare Board Educational Assistance**
- **Other available Tamil Nadu Government scheme documents**

> **Note:** The system provides information based on the official documents available in its knowledge base.

## 🧪 Testing & Test Cases

The application was tested using different types of government scheme-related queries.

| Test Case | Query Type | Expected Result | Result |
|---|---|---|---|
| **TC01** | Tamil Nadu Labour Welfare Board Educational Assistance | Retrieve relevant scheme information, eligibility-related details, and required documents from official sources. | **Pass** |
| **TC02** | PM Vishwakarma | Provide scheme details, eligibility conditions, benefits, and required documents based on retrieved documents. | **Pass** |
| **TC03** | Pudhumai Penn | Identify the government department responsible for the scheme using the available official information. | **Pass** |

### Test Queries

**TC01 – Tamil Nadu Labour Welfare Board Educational Assistance**

> Explain the Tamil Nadu Labour Welfare Board Educational Assistance scheme and tell me what information and documents are needed to determine eligibility.

**TC02 – PM Vishwakarma**

> What is the PM Vishwakarma scheme, who is eligible for it, what benefits are provided, and what documents are required?

**TC03 – Pudhumai Penn**

> Which government department is responsible for the Pudhumai Penn scheme?

### Testing Outcome

The application successfully retrieved relevant information for all three test cases and generated responses based on the retrieved government documents.

The tests demonstrate that CivicGuide AI can handle different types of natural-language queries related to government schemes, including scheme information, eligibility-related details, benefits, required documents, and responsible departments.

---

## 🚀 Deployment

CivicGuide AI has been deployed using **Streamlit Community Cloud** and is publicly accessible through the following link:

👉 **Live Application:**  
https://civicguide-ai-cojbj9ndsvi8rtiemia7fz.streamlit.app/

The deployed application provides the complete workflow:

```text
User Profile
     ↓
User Question
     ↓
Query Processing
     ↓
FAISS Retrieval
     ↓
Relevant Government Documents
     ↓
RAG Context
     ↓
Groq API
     ↓
GPT-OSS-120B
     ↓
Generated Response
```

---

## 🔐 API Key Security

The Groq API key is **not stored directly in the source code**.

For local development, environment variables are used through a `.env` file.

For deployment, the API key is stored securely using **Streamlit Secrets**.

---

## ⚠️ Limitations

Although CivicGuide AI provides useful government scheme-related information, the system has some limitations:

- The system can only answer based on the information available in its knowledge base.
- It does not directly verify a citizen's eligibility with a government department.
- The accuracy of the response depends on the quality and completeness of the retrieved government documents.
- Government schemes, eligibility conditions, benefits, and procedures may change over time.
- The system does not replace official government application or verification processes.
- Internet-based real-time verification of government records is not currently implemented.
- If relevant information is not available in the knowledge base, the system may not be able to provide a complete answer.

> **Important:** Users should refer to the concerned government department or official government portal for final eligibility confirmation and application procedures.

## 🔮 Future Enhancements

The following enhancements can be implemented in future versions of CivicGuide AI:

### 🌐 Expanded Government Knowledge Base

Add more government schemes and services from Central and State Governments to increase the coverage of the system.

### 🗣️ Multilingual Support

Add support for regional Indian languages such as **Tamil, Hindi, Telugu, Malayalam, and Kannada** to make government information more accessible.

### 🎯 Advanced Eligibility Matching

Develop a more structured eligibility-matching system that compares the user's profile with multiple eligibility criteria of different schemes.

### 🔄 Automatic Document Updates

Automatically update the knowledge base whenever new official government guidelines, notifications, or scheme documents are released.

### 📱 Mobile-Friendly Application

Improve the user interface for mobile devices or develop a dedicated mobile application for easier access.

### 🏛️ Government Portal Integration

Integrate official government portals and APIs, where available, to provide updated scheme information and relevant application links.

### 📊 Personalized Scheme Recommendations

Recommend potentially relevant government schemes based on the user's **age, education, income, occupation, location, and other eligibility-related information**.

### 🔊 Voice-Based Assistance

Add speech-to-text and text-to-speech features so users can interact with CivicGuide AI using voice.

### 🔍 Improved Retrieval

Implement advanced retrieval techniques such as **hybrid search, reranking, and metadata-based filtering** to improve the relevance of retrieved information.

### 📈 Analytics and Feedback

Add an optional feedback mechanism to understand user needs and improve the quality of responses and document retrieval.

> These enhancements can further improve the **accuracy, accessibility, personalization, and usability** of CivicGuide AI.

---

## 🏁 Conclusion

CivicGuide AI demonstrates how **Generative AI and Retrieval-Augmented Generation (RAG)** can be used to make government scheme information easier to access and understand.

By retrieving information from official government documents and generating natural-language responses, the system helps users find relevant information about **government schemes, eligibility-related conditions, benefits, required documents, and responsible departments** more efficiently.

The project successfully combines **FAISS vector retrieval, Hugging Face Sentence Transformers, LangChain, Streamlit, Groq API, and GPT-OSS-120B** to develop a practical real-world AI application.

Overall, CivicGuide AI provides a simple, intelligent, and source-grounded approach to improving access to government welfare information while reducing the need to manually search through lengthy official documents.

> **Disclaimer:** CivicGuide AI is an informational AI assistant. It does not provide official eligibility verification or replace government authorities, official portals, or application procedures. Users should verify important information with the concerned government department before taking official action.

---

## 👥 Team QuadraMind

### 🧠 QuadraMind

**Four Minds. One Innovation.**

CivicGuide AI was developed by **Team QuadraMind** as a collaborative Generative AI project focused on improving access to government scheme information.

> **Making Government Services Simple, Accessible, and Intelligent.**

---

### 🚀 Project Highlights

- 🤖 **Generative AI**
- 🔎 **Retrieval-Augmented Generation (RAG)**
- 📚 **Official Government Knowledge Base**
- 🧠 **FAISS Vector Search**
- ⚡ **Groq API + GPT-OSS-120B**
- 🎯 **Personalized User Context**
- 🛡️ **Source-Grounded Responses**
- 🌐 **Streamlit Web Application**
- ☁️ **Public Cloud Deployment**

---

### 💙 Built with Teamwork

**QuadraMind — Four Minds. One Innovation.**

*Designed, developed, tested, and deployed with a focus on making government information simpler and more accessible.*

---

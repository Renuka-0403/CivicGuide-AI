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

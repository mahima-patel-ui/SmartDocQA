





📄 SmartDocQA — AI-Powered Document Question Answering App
🔍 Overview
SmartDocQA is an AI-powered app that answers user questions by extracting relevant information from uploaded PDF documents. It uses Retrieval-Augmented Generation (RAG) for high-accuracy responses.

💡 Features
Upload any PDF document

Ask natural language questions

Get answers based on actual content

Built with Streamlit, PyMuPDF (fitz), and LangChain

🧠 Tech Stack
Python 3.10+

Streamlit

PyMuPDF for PDF parsing

LangChain for RAG-based QA

OpenAI (or any LLM API)

🚀 How to Run the App
Clone the repo or download the folder

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
📁 Folder Structure
graphql
Copy
Edit
SmartDocQA/
├── app.py               # Streamlit interface
├── rag_pipeline.py      # RAG logic for question answering
├── utils.py             # PDF loader with fitz (PyMuPDF)
├── requirements.txt     # All Python dependencies
├── README.md            # Project documentation
└── sample_docs/         # (Optional) Add example PDFs here
📌 Sample Usage
✅ Upload: AI_Assessment.pdf
🗣 Ask: “What is the assignment about?”
📥 Output: “Zeno Talent AI/ML Internship … assessment focuses on programming, data handling, etc.”

🎯 Objective for Yardstick AI
This project demonstrates my ability to:

Implement RAG pipelines

Integrate LLM APIs

Build production-ready tools

Optimize user experience with Streamlit

🙋‍♀️ Created By
Mahima Patel
Email: mahimapatel523@gmail.com
Location: Silwani, Madhya Pradesh
Seeking: Remote AI/ML internship opportunity


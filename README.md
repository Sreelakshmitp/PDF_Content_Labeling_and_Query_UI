# 📄 PDF Content Labeling + Metadata Query (Gemini AI)

This project provides a UI-based tool for extracting, labeling, and querying PDF content using Google's Gemini AI and Streamlit.

<img width="1034" height="393" alt="Screenshot 2025-07-16 145215" src="https://github.com/user-attachments/assets/a445a537-ee39-4336-82b9-45bf394f29c3" />

<img width="1896" height="977" alt="1" src="https://github.com/user-attachments/assets/a938c968-4fa6-4c88-9cb3-64e0e770f33c" />


## 🎯 Objective
- Extract and label content from any PDF using AI (Gemini 1.5 model)
- Allow users to query metadata or labeled content through a clean Streamlit interface

## 🚀 Features
- ✅ Upload and process PDF files page-by-page
  <img width="1897" height="926" alt="2" src="https://github.com/user-attachments/assets/f5dc504b-9f69-4f62-a377-2e84b05fbcf4" />

- ✅ Uses PyMuPDF to extract raw text per page
  <img width="1878" height="858" alt="3" src="https://github.com/user-attachments/assets/387ea6c0-06f0-449e-8e91-9fa9b078818a" />

- ✅ Sends each page to Gemini 1.5 Flash for structured labeling (Title, Code, Paragraph, etc.)
<img width="1852" height="888" alt="6" src="https://github.com/user-attachments/assets/94963e53-2861-4146-82dd-38912a1d73be" />

- ✅ Users can query document metadata or content using LLM
  
<img width="1857" height="657" alt="7" src="https://github.com/user-attachments/assets/929b2d04-42df-427c-8fa8-8d607b6c799e" />

## ⚙️ Setup Instructions
1. Clone the repo  
2. Install dependencies  
3. Add your Gemini API key to `gemini_key.txt`  
4. Run: `streamlit run app.py`

   <img width="1908" height="995" alt="8" src="https://github.com/user-attachments/assets/29b494dd-9846-45a0-9887-3bb6873beba1" />


## 🧪 Evaluation Method (see separate report)

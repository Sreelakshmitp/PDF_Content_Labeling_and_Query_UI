# 📄 PDF Content Labeling + Metadata Query (Gemini AI)

This project provides a UI-based tool for extracting, labeling, and querying PDF content using Google's Gemini AI and Streamlit.


## 📁 Project Structure

```
├── app.py                  # Streamlit UI
├── labeling_utils.py       # Gemini LLM interaction for labeling
├── pdf_utils.py            # PDF text extraction
├── requirements.txt        # Dependencies
├── sample_outputs/
│   └── labeled_sample.json # Sample Gemini response
├── logs/
│   └── interaction.log     # LLM request/response log
```

<img width="1896" height="977" alt="1" src="https://github.com/user-attachments/assets/a938c968-4fa6-4c88-9cb3-64e0e770f33c" />


## 🎯 Objective
- Extract and label content from any PDF using AI (Gemini 1.5 model)
- Allow users to query metadata or labeled content through a clean Streamlit interface

## 🚀 Features
- Upload any PDF and extract page-wise text using PyMuPDF
- Use Gemini AI (1.5 Flash) to label content as Title, Heading, Paragraph, Code, etc.
- Display structured labeled output on the web UI
- Ask natural language questions about the document contents and structure
- Handles LLM errors and provides feedback on failures

- ✅ Upload and process PDF files page-by-page
  <img width="1897" height="926" alt="2" src="https://github.com/user-attachments/assets/f5dc504b-9f69-4f62-a377-2e84b05fbcf4" />

- ✅ Uses PyMuPDF to extract raw text per page
  <img width="1878" height="858" alt="3" src="https://github.com/user-attachments/assets/387ea6c0-06f0-449e-8e91-9fa9b078818a" />

- ✅ Sends each page to Gemini 1.5 Flash for structured labeling (Title, Code, Paragraph, etc.)
<img width="1852" height="888" alt="6" src="https://github.com/user-attachments/assets/94963e53-2861-4146-82dd-38912a1d73be" />

- ✅ Users can query document metadata or content using LLM
  
<img width="1857" height="657" alt="7" src="https://github.com/user-attachments/assets/929b2d04-42df-427c-8fa8-8d607b6c799e" />


 Setup Instructions

1. Clone this repository:
https://github.com/Sreelakshmitp/PDF_Content_Labeling_and_Query_UI


2. Install dependencies:
pip install -r requirements.txt


3. Add your Gemini API Key:
gemini_key.txt

4. Run the app:
streamlit run app.py

   <img width="1908" height="995" alt="8" src="https://github.com/user-attachments/assets/29b494dd-9846-45a0-9887-3bb6873beba1" />


 🧪 Evaluation Method 

Sample Query

User: "What innovations are described in the document?"  
Gemini Response: "AI, Quantum Computing, AR/VR, Biotech, 5G, Blockchain, and Robotics."

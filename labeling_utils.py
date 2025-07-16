import google.generativeai as genai
import json

def load_gemini_key():
    with open("gemini_key.txt", "r") as f:
        return f.read().strip()

def label_content_with_gemini(pages):
    api_key = load_gemini_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    labeled_data = []

    for page in pages:
        prompt = f"""
You are a strict JSON generator. Given a PDF page's raw text, extract labeled sections.

⚠️ Return only valid JSON array. No explanations, no markdown, no extra text. Only a JSON array.

Output format:
[
  {{"label": "Title", "content": "Plagiarism Detection System"}},
  {{"label": "Heading", "content": "1. Install Dependencies"}}
]

Allowed labels: Title, Heading, Paragraph, Table, Code, Bullet, Footer, Metadata, Other.

--- BEGIN PDF PAGE TEXT ---
{page['text']}
--- END ---
"""
        try:
            response = model.generate_content(prompt)
            raw = response.text.strip()
            json_start = raw.find("[")
            json_end = raw.rfind("]")
            if json_start == -1 or json_end == -1:
                raise ValueError("Gemini response does not contain a valid JSON array.")
            json_text = raw[json_start:json_end + 1]
            json.loads(json_text)
            labeled_data.append({ "page": page["page"], "labels": json_text })
        except Exception as e:
            labeled_data.append({ "page": page["page"], "labels": f"Error: {str(e)}" })
    return labeled_data
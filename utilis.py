import os
import PyPDF2
import markdown
from typing import List

def load_txt(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def load_pdf(filepath: str) -> str:
    text = ''
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

def load_md(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = markdown.markdown(f.read())
        return html.replace('\n', ' ')  # simple cleanup

def load_document(filepath: str) -> str:
    ext = os.path.splitext(filepath)[1].lower()
    if ext == '.pdf':
        return load_pdf(filepath)
    elif ext == '.txt':
        return load_txt(filepath)
    elif ext == '.md':
        return load_md(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

import spacy
import PyPDF2
import re

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

# Simple skill keywords list - you can expand this
SKILLS = ['Python', 'Java', 'C++', 'SQL', 'Machine Learning', 'Deep Learning', 'NLP', 'Communication']

# Simple education keywords to search for degrees
EDUCATION_KEYWORDS = ['Bachelor', 'Master', 'B.Sc', 'M.Sc', 'B.Tech', 'M.Tech', 'PhD', 'Doctorate']

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            return ent.text
    return "Name not found"

def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if re.search(r'\b' + re.escape(skill) + r'\b', text, re.I):
            found_skills.append(skill)
    return found_skills

def extract_education(text):
    found_education = []
    for keyword in EDUCATION_KEYWORDS:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text, re.I):
            found_education.append(keyword)
    return found_education

if __name__ == "__main__":
    pdf_file = "sample_resume.pdf"  # Change to your resume file path
    text = extract_text_from_pdf(pdf_file)

    print("Extracted Text:\n", text[:500], "\n")  # Show first 500 chars

    name = extract_name(text)
    skills = extract_skills(text)
    education = extract_education(text)

    print("Name:", name)
    print("Skills:", skills)
    print("Education:", education)

import spacy
import PyPDF2
import re

nlp = spacy.load('en_core_web_sm')

SKILLS = ['Python', 'Java', 'C++', 'SQL', 'Machine Learning', 'Deep Learning', 'NLP', 'Communication']
EDUCATION_KEYWORDS = ['Bachelor', 'Master', 'B.Sc', 'M.Sc', 'B.Tech', 'M.Tech', 'PhD', 'Doctorate']

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove excessive whitespace/newlines
    return text.strip()

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return clean_text(text)

# List of common tech terms to exclude as names

import re

def extract_name(text):
    # List of keywords to ignore that are common in resumes
    IGNORE_WORDS = {
        'html', 'css', 'javascript', 'python', 'java', 'c++', 'sql', 'react', 'node', 'angular',
        'aws', 'git', 'linux', 'docker', 'kubernetes', 'excel', 'powerpoint', 'linkedin', 'github',
        'objective', 'skill', 'skills', 'experience', 'education', 'certification', 'project',
        'resume', 'contact', 'phone', 'email'
    }

    # Take only the first few lines to improve speed and precision
    lines = text.strip().split('\n')[:5]

    for line in lines:
        # Split line by common separators
        parts = re.split(r'[|,-]', line.lower())

        for part in parts:
            candidate = part.strip()
            # Remove digits and special characters for checking
            candidate_clean = re.sub(r'[^a-zA-Z ]', '', candidate)

            # Skip if empty, has digits, or is a known ignore word
            if not candidate_clean or any(word in candidate_clean.split() for word in IGNORE_WORDS):
                continue

            # Assume the candidate is a name if it's 1-4 words long and alphabetic
            words = candidate_clean.split()
            if 1 <= len(words) <= 4:
                # Capitalize words (best guess for name)
                name = ' '.join(w.capitalize() for w in words)
                return name

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

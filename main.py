from parser import extract_text_from_pdf, extract_name, extract_skills, extract_education
from ranker import rank_resume
import spacy
import re
from collections import Counter

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def extract_keywords_from_text(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop:
            keywords.append(token.lemma_.lower())

    common = [kw for kw, _ in Counter(keywords).most_common(20)]
    return list(set(common))  # Remove duplicates

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[\s\-]?)?(\(?\d{3}\)?[\s\-]?)?\d{3}[\s\-]?\d{4}', text)
    return match.group(0) if match else "Not found"

def main():
    resume_file = "sample_resume.pdf"
    jd_file = "job_description.txt"

    try:
        with open(jd_file, "r") as f:
            jd_text = f.read()
            jd_text = clean_text(jd_text)
    except FileNotFoundError:
        print(f"❌ Error: '{jd_file}' not found.")
        return

    keywords = extract_keywords_from_text(jd_text)
    print("\n🔍 Keywords extracted from Job Description:")
    print(keywords)

    try:
        resume_text = extract_text_from_pdf(resume_file)
    except FileNotFoundError:
        print(f"\n❌ Error: '{resume_file}' not found.")
        return

    name = extract_name(resume_text)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)

    print(f"\n👤 Name: {name}")
    print(f"📧 Email: {email}")
    print(f"📱 Phone: {phone}")

    score, missing = rank_resume(resume_text, keywords)

    print(f"\n✅ Resume Score: {score}/{len(keywords)}")

    if score < len(keywords) * 0.6:
        print("\n📌 Suggested Improvements:")
        print("Try including these keywords in your resume:")
    else:
        print("\n🎉 Great job! Your resume matches the job description well. Just to make it better you can check out some more keywords.")
        for kw in missing:
            print(f"- {kw}")

if __name__ == "__main__":
    main()

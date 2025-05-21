import spacy

nlp = spacy.load("en_core_web_md")  # Medium model with vectors, install with: python -m spacy download en_core_web_md

def rank_resume(resume_text, keywords, threshold=0.6):
    doc_resume = nlp(resume_text)
    resume_sentences = list(doc_resume.sents)
    matched_keywords = []
    missing_keywords = []

    for keyword in keywords:
        keyword_doc = nlp(keyword)
        if not keyword_doc.has_vector:
            # Skip or you could add exact match fallback here
            continue

        matched = False
        keyword_lower = keyword.lower()

        for sentence in resume_sentences:
            sentence_text = sentence.text.lower()
            # Check exact substring match OR semantic similarity
            if keyword_lower in sentence_text:
                matched = True
                break
            elif sentence.has_vector and keyword_doc.similarity(sentence) > threshold:
                matched = True
                break

        if matched:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    score = len(matched_keywords)
    return score, missing_keywords



if __name__ == "__main__":
    # Example resume text
    resume_text = """
    Experienced Python developer with knowledge of machine learning and data science.
    Skilled in teamwork and problem solving.
    """

    # Keywords to look for (e.g., from a job description)
    keywords = [
        "Python", "machine learning", "data science", "java",
        "teamwork", "leadership", "communication", "problem solving"
    ]

    score, missing = rank_resume(resume_text, keywords)
    total = len(keywords)

    print(f"✅ Resume Score: {score}/{total}\n")

    
# resumeLens

## Introduction:

resumeLens is a Python tool designed to help you improve your resume by comparing it with a job description. It extracts your contact details from your resume, identifies important keywords from the job description, and checks how well your resume matches those keywords.
This helps you understand which skills or terms you might be missing, so you can make your resume stronger and increase your chances of getting hired.

---

## Features: 

- Automatically extracts your Name, Email, and Phone Number from your resume.
- Identifies important keywords from the job description.
- Checks for both exact and similar keyword matches in your resume.
- Gives you a score that shows how well your resume fits the job.
- Lists suggested keywords to include for a better match.

---

## Requirements: 
To run this project, you will need:  
- Python 3.8 or later
- spaCy library with English medium model
 

---

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/salonikhemka/resumeLens.git
2. Navigate to the project directory:
   ```bash
   cd resumeLens
3. Install required Python libraries:
   ```bash
   pip install spacy
   python -m spacy download en_core_web_md
4. Run the spam detector script:
   ```bash
   python spam.py

---

### Files Description:
- **main.py:** This is the main program you run to analyze a resume. It handles reading the resume text, loading the job description keywords, and showing the final score along with suggestions.
- **ranker.py:** Contains the core logic for checking how well the resume matches the job description. It looks for keywords in the resume and calculates a score based on matches and missing terms.
- **parser.py:** This module is responsible for extracting useful information from resumes. It reads the resume file (like PDF or DOCX), processes the text, and breaks it down into manageable parts so the ranking system can analyze it effectively. Think of it as the part that “understands” the resume content before scoring it.

---

### License:

This project is licensed under the MIT License - see the LICENSE file for details.

---
### Sample Output:
```bash
 Name: XYZ
 Email: xyz@gmail.com
 Phone: 1234567890

 Resume Score: 14/20

 Suggested Improvements:
Try including these keywords in your resume:
- understanding
- willingness
- team
- developer



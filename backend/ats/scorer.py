from backend.ats.keywords import TECH_KEYWORDS

def calculate_ats_score(resume_text):
    resume_text = resume_text.lower()
    matched_keywords = []
    for keyword in TECH_KEYWORDS:
        if keyword in resume_text:
            matched_keywords.append(keyword)
    score = int(len(matched_keywords) / len(TECH_KEYWORDS) * 100)
    missing_keywords = [
        kw for kw in TECH_KEYWORDS 
        if kw not in matched_keywords]
    
    return {
        "score": score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords
    }


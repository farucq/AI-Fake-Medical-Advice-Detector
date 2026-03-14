danger_keywords = [
    "cure cancer",
    "miracle cure",
    "stop medication",
    "replace vaccine",
    "anti vaccine",
    "vaccine causes autism",
    "instant cure",
    "natural cure for cancer"
]

def detect_severity(text):

    text_lower = text.lower()

    for keyword in danger_keywords:
        if keyword in text_lower:
            return "High Risk Advice"

    return "Normal"

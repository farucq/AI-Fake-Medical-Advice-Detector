from models.load_models import classifier
from nlp.preprocessing import preprocess

def classify_advice(text):

    processed = preprocess(text)

    result = classifier(processed)[0]

    label = result["label"]
    confidence = result["score"]

    if label == "NEGATIVE":
        classification = "Misinformation"
    else:
        classification = "Medically Correct"

    return classification, confidence

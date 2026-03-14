from models.load_models import nlp

def extract_medical_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append((ent.text, ent.label_))

    return entities

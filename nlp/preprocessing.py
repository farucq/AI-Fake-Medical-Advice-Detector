from models.load_models import nlp

def preprocess(text):

    doc = nlp(text)

    tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return " ".join(tokens)

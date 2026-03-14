import spacy
from transformers import pipeline
from sentence_transformers import SentenceTransformer

# Load NLP model
nlp = spacy.load("en_core_sci_sm")

# Sentence embeddings
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Classification model
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    return_all_scores=True
)

# Explanation model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

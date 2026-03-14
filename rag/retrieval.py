import numpy as np
import faiss

from models.load_models import embedding_model
from rag.knowledge_base import knowledge_base

embeddings = embedding_model.encode(knowledge_base)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def retrieve_medical_knowledge(query):

    query_vector = embedding_model.encode([query])

    D, I = index.search(np.array(query_vector), k=2)

    results = [knowledge_base[i] for i in I[0]]

    return results

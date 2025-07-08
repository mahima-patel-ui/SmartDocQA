from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_and_retrieve(user_question, documents):
    if not documents:
        return "No documents provided."

    # Split PDF into paragraphs or chunks
    text_chunks = []
    for doc in documents:
        chunks = [p.strip() for p in doc.split("\n\n") if len(p.strip()) > 30]
        text_chunks.extend(chunks)

    # Embed all chunks and the user question
    chunk_embeddings = model.encode(text_chunks)
    question_embedding = model.encode([user_question])

    # Find the most similar chunk
    similarity_scores = cosine_similarity(question_embedding, chunk_embeddings)
    best_index = similarity_scores.argmax()
    best_chunk = text_chunks[best_index]

    return best_chunk



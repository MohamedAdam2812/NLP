4. 🔹 RoBERTa Similarity Code


from transformers import RobertaTokenizer, RobertaModel

from sklearn.metrics.pairwise import cosine_similarity

token = RobertaTokenizer.from_pretrained("roberta-base")

model = RobertaModel.from_pretrained("roberta-base")

p1 = "The language learning platform helps users improve vocabulary."

p2 = "This system suggests synonyms to expand vocabulary."

emb1 = model(**token(p1, return_tensors="pt")).last_hidden_state.mean(1).detach()

emb2 = model(**token(p2, return_tensors="pt")).last_hidden_state.mean(1).detach()

score = cosine_similarity(emb1, emb2)[0][0]

level = "High" if score>=0.75 else "Medium" if score>=0.40 else "Low"

print("RoBERTa Score:", score)

print("Similarity Level:", level)

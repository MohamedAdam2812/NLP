import spacy

nlp = spacy.load("en_core_web_sm")

text = """Wow, yesterday Dr. Arun Kumar, the chief scientist of India, announced that he will quickly launch three innovative AI-based projects in Chennai because they can significantly improve safety. It may not only reduce accidents but also save lives. There are over 50 experts working on the projects."""

doc = nlp(text)

for token in doc:
    print(token.text, "->", token.pos_)


import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Example text
text = "Kingsley is a good boy"

# Process the text with SpaCy NLP pipeline
doc = nlp(text)

# Print POS tags for each token in the text
for token in doc:
    print(f"Word: {token.text}, POS: {token.pos_}")

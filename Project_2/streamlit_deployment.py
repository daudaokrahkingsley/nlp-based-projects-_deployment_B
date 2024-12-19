import spacy
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt


nlp = spacy.load("en_core_web_sm")


st.title("Part Of Speech Tagging")


text = st.text_area("Enter a text")


if st.button('Generate Analysis'):
     
    doc = nlp(text)

    
    word_count = len([token for token in doc if not token.is_space])  # Count tokens that are not spaces

    
    space_count = len([token for token in doc if token.is_space])  # Count spaces

    st.write(f"**Word Count**: {word_count}")
    

    st.write("Part of Speech Tags:")
    for token in doc:
        st.write(f"Word: {token.text}, POS: {token.pos_}")

    st.write("### WordCloud of the Text:")
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")  

   
    st.pyplot(fig)

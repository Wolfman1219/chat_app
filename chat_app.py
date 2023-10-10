import streamlit as st
import requests
from topic_extraction import get_answer
from googletrans import Translator
translator = Translator()

def main():
    st.title("Chat App")
    question = st.text_input("Savolingizni bering:")
    if st.button("Ask"):
        # Call your API to get the answer here
        question = translator.translate(question, dest='en')
        print(question)
        answer = get_answer(question.text)
        answer = translator.translate(answer, dest = 'uz')
        st.text(f"Answer: {answer.text}")

if __name__ == "__main__":
    main()

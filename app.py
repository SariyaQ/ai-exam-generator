import streamlit as st
from src.prompt_builder import build_prompt

st.title("AI Exam Generator")

st.write("Generate structured exam prompts for teachers.")

grade = st.selectbox("Grade", [5, 6, 7, 8, 9, 10, 11])
subject = st.text_input("Subject", value="ICT")
topic = st.text_input("Topic", value="Algorithms")
difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
question_count = st.slider("Number of Questions", 1, 20, 5)

if st.button("Generate Prompt"):
    prompt = build_prompt(
        grade=grade,
        subject=subject,
        topic=topic,
        difficulty=difficulty,
        question_count=question_count
    )

    st.subheader("Generated Prompt")
    st.code(prompt, language="text")


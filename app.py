import streamlit as st
from src.prompt_builder import build_prompt
from src.openai_client import generate_exam
from src.pdf_generator import generate_pdf
st.title("AI Exam Generator")

st.write("Generate structured exam questions for teachers.")

grade = st.selectbox("Grade", [5, 6, 7, 8, 9, 10, 11])
subject = st.text_input("Subject", value="ICT")
topic = st.text_input("Topic", value="Algorithms")
difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
question_type = st.selectbox(
    "Question Type",
    ["Multiple Choice", "True/False", "Short Answer", "Mixed"]
)
question_count = st.slider("Number of Questions", 1, 20, 5)

if st.button("Generate Exam"):
    prompt = build_prompt(
        grade=grade,
        subject=subject,
        topic=topic,
        difficulty=difficulty,
        question_count=question_count,
        question_type=question_type

    )

    st.subheader("Generated Prompt")
    st.code(prompt, language="text")

    with st.spinner("Generating exam..."):
        exam = generate_exam(prompt)

    st.subheader("Generated Exam")

for q in exam.questions:
    st.markdown(f"### Question {q.id}")
    st.write(q.question)

    st.write(f"A. {q.options.A}")
    st.write(f"B. {q.options.B}")
    st.write(f"C. {q.options.C}")
    st.write(f"D. {q.options.D}")

    st.success(f"Correct Answer: {q.correct_answer}")
    st.info(f"Explanation: {q.explanation}")

    st.caption(
        f"Topic: {q.topic} | Difficulty: {q.difficulty} | Bloom Level: {q.bloom_level}"
    )

    st.divider()
    pdf = generate_pdf(exam)

st.download_button(
    label="📄 Download PDF",
    data=pdf,
    file_name="AI_Exam.pdf",
    mime="application/pdf",
)




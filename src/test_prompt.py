from prompt_builder import build_prompt

prompt = build_prompt(
    grade=7,
    subject="ICT",
    topic="Algorithms",
    difficulty="Medium",
    question_count=5
)

print(prompt)


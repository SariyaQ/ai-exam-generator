def build_prompt(
    grade,
    subject,
    topic,
    difficulty,
    question_count
):
    with open(
        "prompts/exam_prompt.txt",
        "r"
    ) as file:

        template = file.read()

    prompt = template.format(
        grade=grade,
        subject=subject,
        topic=topic,
        difficulty=difficulty,
        question_count=question_count
    )

    return prompt


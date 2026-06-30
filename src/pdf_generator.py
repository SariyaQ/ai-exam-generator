from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from src.schemas import Exam


def generate_pdf(exam: Exam) -> bytes:
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Generated Exam</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    for question in exam.questions:
        elements.append(
            Paragraph(
                f"<b>Question {question.id}:</b> {question.question}",
                styles["Heading2"],
            )
        )

        elements.append(Paragraph(f"A. {question.options.A}", styles["BodyText"]))
        elements.append(Paragraph(f"B. {question.options.B}", styles["BodyText"]))
        elements.append(Paragraph(f"C. {question.options.C}", styles["BodyText"]))
        elements.append(Paragraph(f"D. {question.options.D}", styles["BodyText"]))

        elements.append(
            Paragraph(
                f"<b>Answer:</b> {question.correct_answer}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"<b>Explanation:</b> {question.explanation}",
                styles["BodyText"],
            )
        )

        elements.append(
            Paragraph(
                f"Topic: {question.topic} | Difficulty: {question.difficulty} | Bloom: {question.bloom_level}",
                styles["Italic"],
            )
        )

        elements.append(Spacer(1, 15))

    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf

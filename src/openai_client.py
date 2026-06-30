from openai import OpenAI
from dotenv import load_dotenv
from src.schemas import Exam

load_dotenv()

client = OpenAI()


def generate_exam(prompt):
    response = client.responses.parse(
        model="gpt-4.1-mini",
        input=prompt,
        text_format=Exam
    )

    return response.output_parsed


from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_exam(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0.3
    )

    return response.output_text


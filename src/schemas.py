from pydantic import BaseModel
from typing import List


class Options(BaseModel):
    A: str
    B: str
    C: str
    D: str


class Question(BaseModel):
    id: int
    question: str
    question_type: str
    topic: str
    difficulty: str
    bloom_level: str
    options: Options
    correct_answer: str
    explanation: str


class Exam(BaseModel):
    questions: List[Question]

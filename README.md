# 🤖 AI Exam Generator

An AI-powered web application that helps teachers generate high-quality exam questions in seconds using OpenAI's language models.

The application allows teachers to customize exams by grade, subject, topic, difficulty level, question type, and number of questions. Generated exams can be previewed and downloaded as PDF files.

---

## ✨ Features

* 🤖 AI-powered exam generation using OpenAI API
* 📚 Multiple subjects and grade levels
* 🎯 Multiple question types

  * Multiple Choice
  * True/False
  * Short Answer
  * Mixed
* 📊 Difficulty selection

  * Easy
  * Medium
  * Hard
* ✅ Structured Outputs with Pydantic
* 📄 PDF export
* 🌐 Interactive Streamlit interface
* 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

* Python
* Streamlit
* OpenAI API
* Pydantic
* ReportLab
* python-dotenv

---

## 📂 Project Structure

```text
ai-exam-generator/
│
├── app.py
├── requirements.txt
├── prompts/
│   └── exam_prompt.txt
│
├── src/
│   ├── openai_client.py
│   ├── pdf_generator.py
│   ├── prompt_builder.py
│   └── schemas.py
│
└── .env
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/SariyaQ/ai-exam-generator.git
```

Move into the project folder:

```bash
cd ai-exam-generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 📄 Example Workflow

1. Select grade level
2. Enter subject and topic
3. Choose difficulty
4. Select question type
5. Set the number of questions
6. Generate the exam
7. Preview the generated questions
8. Download the exam as a PDF

---

## 🎯 Future Improvements

* Microsoft Word export
* Separate answer key
* Azerbaijani language support
* Bloom's Taxonomy integration
* School branding and logo support
* Streamlit Cloud deployment

---

## 👩‍💻 Author

**Sariya Gasimova**

AI Engineer Portfolio Project

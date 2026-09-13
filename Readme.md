🤖 AI Personal Assistant

A simple and powerful **AI Personal Assistant** built with **Flask** and Google's **Gemini API**.

This project provides two core AI-powered features:

1. 💬 **Ask Anything** — Ask questions in natural language and receive AI-generated answers.
2. 📧 **Summarize Email** — Paste an email and get a concise 2–3 sentence summary.

The application demonstrates how a Flask backend can communicate with a generative AI model and provide the result to a browser-based frontend through REST-style endpoints.

---

## 📌 Features

### 💬 Ask Anything

Users can enter any question into the Personal Assistant and receive an AI-generated response.

Example:

> **Question:** What is hallucination ?

The backend sends the question to Gemini and returns the generated answer to the frontend.

### 📧 Email Summarization

Users can paste the contents of an email into the application.

The AI analyzes the email and generates a short summary, making it easier to understand long messages quickly.

Example:

> **Email:** A long meeting/update email  
> **Output:** A concise 2–3 sentence summary.

### 🌐 Web Interface

The application uses a simple browser-based interface containing:

- Ask Anything section
- Email summarization section
- Input fields
- Buttons for submitting requests
- Loading/processing feedback
- AI response display

### 🔐 Environment Variables

The Gemini API key is stored in a `.env` file rather than directly inside the Python source code.

This keeps sensitive credentials separate from application code.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Flask** | Backend web framework |
| **Google Gemini API** | AI response generation and email summarization |
| **google-genai** | Google GenAI Python SDK |
| **python-dotenv** | Loads environment variables from `.env` |
| **HTML5** | Frontend structure |
| **CSS3** | Frontend styling |
| **JavaScript** | Sends requests to Flask and updates the UI |
| **JSON** | Communication format between frontend and backend |

---


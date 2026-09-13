from flask import Flask,render_template,jsonify,url_for,request
import os
from dotenv import load_dotenv  
from google import genai

load_dotenv()

api_key=os.getenv("API_KEY")
client=genai.Client(api_key=api_key)

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")

    response = client.interactions.create(
        model="gemini-3.8-flash",
        system_instruction="Act like a helpful personal assistant.",
        input=question,
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 512
        }
    )

    answer = response.output_text.strip()
    return jsonify({"response": answer}), 200


@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email")

    prompt = f"""
    Summarize the following email in 2-3 sentences:
    {email_text}
    """

    response = client.interactions.create(
        model="gemini-3.8-flash",
        system_instruction="Act like an expert email assistant.",
        input=prompt,
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 512
        }
    )

    summary = response.output_text.strip()

    return jsonify({"response": summary}), 200


if __name__ == "__main__":
    app.run(debug=True)
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

@app.route("/ask",methods=["POST"])
def query():
    question=request.form.get("question")
    response=client.interactions.create(
        model="gemini-3.8-flash",
        input=[
                {"role": "system", "content": "Act like a helpful personal assistant"},
                {"role": "user", "content": question}
            ],
        temperature=0.7,
        max_output_tokens=512
    )
    answer = response.output_text.strip()
    print(answer)
    return jsonify({"response": answer}), 200


@app.route("/summarize",methods=["POST"])
def query():
    email_text=request.form.get("email")
    prompt=f"summarize the following email in 2-3 sentneces {email_text}"
    response=client.interactions.create(
        model="gemini-3.8-flash",
        input=[
                {"role": "system", "content": "Act like a expert email assistant"},
                {"role": "user", "content": prompt}
            ],
        temperature=0.3,
        max_output_tokens=512
    )
    summary = response.output_text.strip()
    return jsonify({"response": summary}), 200


if __name__ == "__main__":
    app.run(debug=True)
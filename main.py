from flask import Flask,render_template,jsonify
import os
from dotenv import load_dotenv  
from google import genai

load_dotenv()

api_key=os.getenv("API_KEY")

app=Flask(__name__)

@app.route("/")
def query():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
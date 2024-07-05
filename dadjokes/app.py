from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

# Ganti dengan API key Anda
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_joke', methods=['POST'])
def get_joke():
    response = client.chat.completions.create(
        engine="text-davinci-003",
        max_tokens=50,
        messages=[
        {
            "role": "user",
            "content": "Tell me a dad joke.",
        }
    ],
    model="gpt-3.5-turbo",
    )
    joke = response.choices[0].text.strip()
    return {'joke': joke}

if __name__ == '__main__':
    app.run(debug=True)

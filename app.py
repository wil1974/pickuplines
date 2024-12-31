from flask import Flask, render_template, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_api_key():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("GEMINI_API_KEY not found in system environment, checking .env file")
    return api_key

@app.route('/')
def index():
    api_key = get_api_key()
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set.", 500
    return render_template('index.html', api_key=api_key)

@app.route('/generate_pickup_line', methods=['POST'])
def generate_pickup_line():
    api_key = get_api_key()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    prompt_starters = [
        "Generate a short, funny pickup line.",
        "Give me a cheesy pickup line.",
        "Create a witty pickup line.",
        "Write a hilarious pickup line.",
        "Come up with a unique pickup line."
    ]
    import random
    prompt = random.choice(prompt_starters)
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.7
        }
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        json_response = response.json()
        pickup_line = json_response.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "Failed to generate pickup line.")
        return jsonify({'pickupLine': pickup_line})
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return jsonify({'pickupLine': "Failed to generate pickup line."}), 500

if __name__ == '__main__':
    app.run(debug=True)

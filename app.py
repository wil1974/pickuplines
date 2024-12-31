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

from flask import Flask, render_template, jsonify, request
import os
import requests
from dotenv import load_dotenv
import random

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
    
    description = request.get_json().get('description', '')
    
    prompt_starters = [
        f"Generate a short, funny, and unique pickup line about {description}. Make sure the pickup line is different from the other pickup lines you generate.",
        f"Give me a cheesy, but unique pickup line related to {description}. Make sure the pickup line is different from the other pickup lines you generate.",
        f"Create a witty and unique pickup line that includes {description}. Make sure the pickup line is different from the other pickup lines you generate.",
        f"Write a hilarious and unique pickup line about {description}. Make sure the pickup line is different from the other pickup lines you generate.",
        f"Come up with a unique pickup line referencing {description}. Make sure the pickup line is different from the other pickup lines you generate."
    ]
    
    num_lines = 3
    pickup_lines = []
    for _ in range(num_lines):
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
            pickup_lines.append(pickup_line)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            pickup_lines.append("Failed to generate pickup line.")
    
    return jsonify({'pickupLines': pickup_lines})

if __name__ == '__main__':
    app.run(debug=True)

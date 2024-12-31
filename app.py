from flask import Flask, render_template, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return "Error: GEMINI_API_KEY environment variable not set.", 500
    return render_template('index.html', api_key=api_key)

@app.route('/generate_pickup_line', methods=['POST'])
def generate_pickup_line():
    api_key = os.environ.get('GEMINI_API_KEY')
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{
                "text": "Generate a short, funny pickup line."
            }]
        }]
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

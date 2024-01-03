import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import base64

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        print(data)
        token = post_submission(get_language_id(data["language"]), data["code"], "", "")
        result = ''

        while True:
            result = get_submission_result(token)
            if result['status']['id'] > 2:
                print(result)
                return jsonify(result)
            time.sleep(.2)
            
        return result
    
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()

def post_submission(language_id: int, code: str, input: str, expected_output: str):
    url = "https://judge0-ce.p.rapidapi.com/submissions"
    querystring = {"base64_encoded":"true","fields":"*"}

    payload = {
        "language_id": language_id,
        "source_code": base64.b64encode(code.encode()).decode(),
        "stdin": input,
        "expected_output": base64.b64encode(expected_output.encode()).decode()
    }

    headers = {
        "X-RapidAPI-Key": "a13dd8b797msh23f219ceb2841c4p1f8e3djsnd39de1d58a49",
        "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    }

    return requests.post(url, json=payload, headers=headers, params=querystring).json().get('token')

def get_submission_result(token: str):
    url = f"https://judge0-ce.p.rapidapi.com/submissions/{token}"
    querystring = {"base64_encoded":"true","fields":"*"}

    headers = {
        "X-RapidAPI-Key": "a13dd8b797msh23f219ceb2841c4p1f8e3djsnd39de1d58a49",
        "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    }

    return requests.get(url, headers=headers, params=querystring).json()

def get_language_id(language: str):
    if language.strip() == "python":
        return 71
    
    if language.strip() == "c++":
        return 76
    
    if language.strip() == "javascript":
        return 93
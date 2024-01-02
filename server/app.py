from flask import Flask, jsonify
from flask_cors import CORS
import requests
import base64

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()

def post_submission(language_id: int, source_code_path: str, input: str, expected_output: str):
    url = "https://judge0-ce.p.rapidapi.com/submissions"
    querystring = {"base64_encoded":"true","fields":"*"}

    with open(source_code_path, 'r') as file:
        source_code = file.read()

    payload = {
        "language_id": language_id,
        "source_code": base64.b64encode(source_code.encode()).decode(),
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

#result = get_submission_result(post_submission(71, 'Hello_World.py', '', 'Hello Friends!'))
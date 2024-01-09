import requests
import base64

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
    
    if language.strip() == "c_cpp":
        return 54
    
    if language.strip() == "java":
        return 62
    
    if language.strip() == "javascript":
        return 93
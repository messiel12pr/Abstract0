from flask import Flask, jsonify, request
from flask_cors import CORS
import server.utils.judge0_utils as j0_utils
from authlib.integrations.flask_oauth2 import ResourceProtector
from server.utils.validator import Auth0JWTBearerTokenValidator
from server.utils.database import Database
import time

db = Database()

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    "dev-4rrc5mwzkxlwv7kz.us.auth0.com",
    "http://127.0.0.1:5001"
)
require_auth.register_token_validator(validator)

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/problems/<int:id>", methods=['GET'])
def get_problem_location(id):
    response = db.get_problem(id)
    print(response)
    return jsonify(response[0][3])


@app.route("/user/<int:id>/problem-solved-count", methods=['GET'])
@require_auth(None)
def get_problems_solved(id):
    response = db.count_problems_solved(id)
    return jsonify(response)

@app.route("/submit", methods=['POST'])
@require_auth(None)
def submit():
    try:
        data = request.get_json()
        submission_token = j0_utils.post_submission(j0_utils.get_language_id(data["language"]), data["code"], "", "")
        result = ''

        while True:
            result = j0_utils.get_submission_result(submission_token)
            if result['status']['id'] > 2:
                print(result)
                return jsonify(result)
            time.sleep(.2)
            
        return result
    
    except Exception as e:
        return jsonify({'error': e.__str__()})

if __name__ == '__main__':
    app.run()
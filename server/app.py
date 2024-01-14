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

@app.route("/api/public")
def public():
    """No access token required."""
    response = (
        "Hello from a public endpoint! You don't need to be"
        " authenticated to see this."
    )
    return jsonify(message=response)


@app.route("/submit", methods=['POST'])
@require_auth(None)
def submit():
    """A valid access token is required."""

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
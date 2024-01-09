import time
from flask import Flask, jsonify, request
from flask_cors import CORS
import server.utils.judge0_utils as j0_utils

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
        auth_token = request.headers['Authorization'].split('Bearer ')[1]
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
        print(str(e))
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run()
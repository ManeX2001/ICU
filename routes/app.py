from flask import Blueprint, jsonify, request

# Make sure this line is present exactly as below:
api = Blueprint('api', __name__)

@api.route('/hospital-status', methods=['GET'])
def get_hospital_status():
    # … your code …
    return jsonify(hospital_status)

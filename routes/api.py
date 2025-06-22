# API routes
# routes/api.py
from flask import Blueprint, jsonify, request

# Define the blueprint exactly as “api”
api = Blueprint('api', __name__)

@api.route('/hospital-status', methods=['GET'])
def get_hospital_status():
    """
    Return current hospital status as JSON. Placeholder data for now.
    """
    hospital_status = {
        'icu': {
            'occupied': 7,
            'capacity': 10,
            'utilization': 70,
            'status': 'Normal',
            'definition': 'Critical care unit'
        },
        'ward': {
            'occupied': 25,
            'capacity': 40,
            'utilization': 62.5,
            'status': 'High',
            'definition': 'General inpatient unit'
        },
        'ed': {
            'occupied': 18,
            'capacity': 30,
            'utilization': 60,
            'status': 'Busy',
            'definition': 'Emergency department'
        }
    }
    return jsonify(hospital_status)


# ---------------------------------------------------------------------------
# API endpoint: /admission-decision
# ---------------------------------------------------------------------------

@api.route('/admission-decision', methods=['POST'])
def admission_decision():
    """Return an admission decision based on provided patient data."""
    # Grab JSON data from the request
    payload = request.get_json() or {}

    # TODO: Integrate a real ML model here. For now, use a simple rule.
    condition = str(payload.get('condition', '')).lower()
    decision = 'admit' if condition == 'severe' else 'discharge'

    return jsonify({'success': True, 'result': decision})

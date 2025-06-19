from flask import Blueprint, render_template

# Main blueprint for hospital dashboard, analytics, and patient form
main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    """
    Render the main hospital dashboard with current status data.
    """
    # TODO: Replace with real data loading logic
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
    return render_template('dashboard.html', hospital_status=hospital_status)

@main.route('/analytics')
def analytics():
    """
    Render the analytics page.
    """
    return render_template('analytics.html')

@main.route('/patient-form')
def patient_form():
    """
    Render the new patient assessment form page.
    """
    return render_template('patient_form.html')

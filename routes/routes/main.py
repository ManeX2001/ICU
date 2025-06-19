# Main routes
# routes/main.py
from flask import Blueprint, render_template

# ← This name must match what you import in app.py
main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    # pull in your data and render dashboard.html
    return render_template('dashboard.html', hospital_status=...)

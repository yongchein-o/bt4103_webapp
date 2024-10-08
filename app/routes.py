from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')
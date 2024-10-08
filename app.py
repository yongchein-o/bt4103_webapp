# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Pass your Tableau workbook URL to the template
    tableau_url = 'https://prod-apnortheast-a.online.tableau.com/t/ycong-4eb5f52894/views/Book2/dashboard'
    return render_template('index.html', tableau_url=tableau_url)

if __name__ == '__main__':
    app.run(debug=True)
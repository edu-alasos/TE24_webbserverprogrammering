# imports render_template from Flask to render templates
from flask import Flask, render_template, request

"""
    All templates are stored in the 'templates' directory. 
    This is standard for Flask applications.
"""
app = Flask(__name__)

# Define the home route "[ip-adress]:5000". A name can be passed as a query parameter named 'name'.
# Vad händer ifall man skriver t.ex. "localhost:5000?name=Holger" i webbläsaren?
@app.route('/')
def home():
    if not request.args.get('name'):
        name = "World"
    else:
        name = request.args.get('name')
    # Render the index.html template with a name variable
    return render_template('index.html', name=name)

@app.route('/teachers')
def teachers():
    # Define a list of sneakers
    teachers = [
        {'name': 'Holger', 'subject': 'Webbserverprogrammering', 'students': 31},
        {'name': 'Martin', 'subject': 'Webbutveckling', 'students': 32},
        {'name': 'Nikodemus', 'subject': 'Programmering', 'students': 29},
    ]
    # Render the sneakers.html template with a list of sneakers
    return render_template('teachers.html', teachers=teachers)  # testa att ersätta sneakers=sneakers med sneakers=[]

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
# Import the Flask class from the flask module and initialize a Flask application instance
from flask import Flask, request
app = Flask(__name__)

# GET route that displays two forms: one for POST and one for GET
@app.route('/')
def form():
    return '''
        <h1>Form demo</h1>
        <h2>POST form</h2>
        <form action="/post-submit" method="post">
            <label for="data">Enter something:</label>
            <input type="text" id="data" name="data"><br>
            <input type="checkbox" id="checkbox" name="checkbox"><label for="checkbox">Check this</label> <br>
            <input type="submit" value="Submit">
        </form>
        <h2>GET form</h2>
        <form action="/get-submit" method="get">
            <label for="data">Enter something:</label>
            <input type="text" id="data" name="data"><br>
            <input type="checkbox" id="checkbox" name="checkbox"><label for="checkbox">Check this</label> <br>
            <input type="submit" value="Submit">
        </form>
    '''

# Example of a simple POST route that handles POST requests to /post-submit
@app.route('/post-submit', methods=['POST'])
def postsubmit():
    # request.form is a dictionary-like object containing form data
    data = request.form.get('data', '')  #form data is captured here using the name attribute of the input
    checkbox = request.form.get('checkbox', False)

    with open(r"C:\Users\08sosala\Documents\vscode\python\webbserverprogrammering\TE24_webbserverprogrammering\v35\file.txt", "w") as f:
        f.write(f"POST, Data: {data}, Checkbox: {checkbox}\n")

    if data == "abc":
        return "adsfsadfasdfasfd"

    return f'Skickat via POST: {data}, Checkbox: {checkbox}'

# Example of a simple GET route that handles GET requests with URL parameters
@app.route('/get-submit')
def getsubmit():
    # request.args is a dictionary-like object containing query parameters
    data = request.args.get('data', '')
    checkbox = request.args.get('checkbox', False)

    with open(r"C:\Users\08sosala\Documents\vscode\python\webbserverprogrammering\TE24_webbserverprogrammering\v35\file.txt", "a") as f:
        f.write(f"GET, Data: {data}, Checkbox: {checkbox}\n")

    if data == "abc":
        return "adsfsadfasdfasfd"

    return f'Skickat via GET: {data}, Checkbox: {checkbox}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
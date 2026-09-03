# En server som använder Flask för att serva HTML-filer och andra s.k. "statiska" filer (bilder, CSS, JavaScript).
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():    # HTML-filen ligger i en mapp med namnet "templates"
    with open(r"C:\Users\08sosala\Documents\vscode\python\webbserverprogrammering\TE24_webbserverprogrammering\v35\file.txt", "r") as f:
        result = f.readlines()
        print(result)
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # filerna servas via din IP-adress i det lokala nätverket
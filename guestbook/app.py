from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():

    with open("TE24_webbserverprogrammering\guestbook\data.json", "r") as f:
        posts = f.readlines()
        json.dumps(posts)
        print(posts)
            
        return render_template("index.html", posts=posts)


@app.route("/send", methods=["POST"])
def send():
    print(request.form)
    name = request.form.get("name")
    mail = request.form.get("mail")
    homepage = request.form.get("homepage")
    phone = request.form.get("phone")
    comment = request.form.get("comment")

    full = {"name": name,
            "mail": mail,
            "homepage": homepage,
            "phone": phone,
            "comment": comment}
    
    encoded = json.JSONEncoder().encode(full)

    with open("TE24_webbserverprogrammering\guestbook\data.json", "a") as f:
        f.write(f"{encoded}\n")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
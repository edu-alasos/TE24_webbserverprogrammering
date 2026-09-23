from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


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
    
    print(full)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
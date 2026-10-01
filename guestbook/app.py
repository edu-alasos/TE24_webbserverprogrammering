from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")


def load_posts():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []


def save_posts(posts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=4, ensure_ascii=False)


@app.route("/")
def index():
    posts = load_posts()
    posts.reverse()
    return render_template("index.html", posts=posts)


@app.route("/send", methods=["POST"])
def send():
    post = {
        "name": request.form.get("name"),
        "mail": request.form.get("mail"),
        "homepage": request.form.get("homepage"),
        "phone": request.form.get("phone"),
        "comment": request.form.get("comment"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    posts = load_posts()
    posts.append(post)
    save_posts(posts)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
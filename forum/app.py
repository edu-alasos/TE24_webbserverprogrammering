from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import os
import mysql

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

def koppla_upp():
    # En ny uppkoppling per anrop, så att den inte hinner "somna" mellan besöken
    return mysql.connector.connect(
        host="localhost",
        user="root",          # standardanvändarnamn för XAMPP
        password="",          # standardlösenord (tom sträng)
        database="bomboclat"  # byt om din databas heter något annat
    )


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
def welcome():
    return render_template("welcome.html")


@app.route("/send", methods=["POST"])
def send():
    post = {
        "name": ,
        "comment": request.form.get("comment"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    posts = load_posts()
    posts.append(post)
    save_posts(posts)

    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    data = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
    }



    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
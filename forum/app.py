from flask import Flask, render_template, request, redirect, g, session
import json
from datetime import datetime
import os
import mysql.connector
import hashlib

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

def load_user():
    g.user = None
    user_id = session.get("user_id")

    if user_id != None:
        db = koppla_upp()
        cursor = db.cursor(dictionary=True)
        g.user = cursor.fetchone()
        db.close()


@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/forum", methods=["POST"])
def forum():

    db = koppla_upp()
    cursor = db.cursor()
    id = session["userid"]
    cursor.execute("SELECT username FROM users (id) VALUES (%s, %s)", id)


    post = {
        "name": "a",
        "comment": request.form.get("comment"),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    posts = load_posts()
    posts.append(post)
    save_posts(posts)

    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login", methods=["POST"])
def login():
    data = {
        "username": request.form.get("username"),
        "password": request.form.get("password"),
    }

    return redirect("/forum")

@app.route("/registerPOST", methods=["POST"])
def registerPOST():
    print(request)
    username = request.form.get("username")
    password = request.form.get("password")

    hashed_password = hashlib.sha1(password.encode())

    db = koppla_upp()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (%s, %s)", username, hashed_password)
    db.commit()

    id = cursor.lastrowid
    session["userid"] = id

    db.close()

    return redirect("/forum")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
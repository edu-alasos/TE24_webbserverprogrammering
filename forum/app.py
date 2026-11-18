from flask import Flask, render_template, request, redirect, g, session
import json
from datetime import datetime
import os
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = "avm340v9a3mv0"

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
    db = koppla_upp()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT users.username, posts.comment, posts.created_at
            FROM posts
            JOIN users ON posts.userid = users.id
            ORDER BY posts.created_at DESC
        """)

        posts = cursor.fetchall()

        return posts
    except:
        return []


def save_posts():
    db = koppla_upp()
    cursor = db.cursor()

    cursor.execute(
    "INSERT INTO posts (userid, comment) VALUES (%s, %s)",
    (session["userid"], request.form.get("comment")),
    )

    db.commit()


def load_user():
    g.user = None
    userid = session.get("userid")

    if userid != None:
        db = koppla_upp()
        cursor = db.cursor(dictionary=True)
        g.user = cursor.fetchone()
        db.close()


@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/forum")
def forum():
    posts = load_posts()

@app.route("/forumSend")
def forumSend():

    db = koppla_upp()
    cursor = db.cursor()
    id = session["userid"]
    cursor.execute("SELECT (id) FROM users WHERE id = %s", (id,))


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

@app.route("/loginPOST", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    hashed_password = hashlib.sha1(password.encode()).hexdigest()

    db = koppla_upp()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        data = cursor.fetchone()
        db.close()
        print(data)
        if data[2] == hashed_password:
            print("success")
            id = data[0]
            session["userid"] = id
        else:
            print("incorrect password")
            return redirect("/")
    except:
        print("username not found")
        return redirect("/")

    return redirect("/forum")

@app.route("/registerPOST", methods=["POST"])
def registerPOST():
    username = request.form.get("username")
    password = request.form.get("password")

    hashed_password = hashlib.sha1(password.encode()).hexdigest()

    db = koppla_upp()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()

    id = cursor.lastrowid
    session["userid"] = id

    db.close()

    return redirect("/forum")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
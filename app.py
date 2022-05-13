from flask import Flask, render_template
from config import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contacts")
def contacts():
    return "this is contact page"


if __name__ == "__main__":
    app.run(debug=True, port=8000)

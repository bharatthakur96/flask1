from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    # return "this is home page"

@app.route("/contacts")
def contacts():
    return "this is contact page"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
 
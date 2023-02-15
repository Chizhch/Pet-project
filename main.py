from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "secret":
            return redirect(url_for("secret"))
        else:
            return "Incorrect login. Please try again."
    return render_template("login.html")

@app.route("/secret")
def secret():
    return "You have successfully logged in!"

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = "SUPER_SECRET_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "user" and password == "U$eR@12345":
        mfa_code = str(random.randint(100000, 999999))
        session["mfa_code"] = mfa_code
        print("\n===== DEMO MFA CODE =====")
        print("Username: user")
        print("MFA CODE:", mfa_code)
        print("=========================\n")
        return redirect(url_for("mfa"))

    return "Invalid credentials"

@app.route("/mfa", methods=["GET", "POST"])
def mfa():
    return render_template("mfa.html")


@app.route("/verify", methods=["POST"])
def verify():
    if request.form["code"] == session.get("mfa_code"):
        return redirect("/dashboard")
    return "Invalid MFA Code"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','brilhah-dev-key')
APP_NAME = os.environ.get('APP_NAME','BRILHAH SHOP AI')
PRIVATE_MODE = os.environ.get('PRIVATE_MODE','1') == '1'

@app.route("/")
def home():
    if PRIVATE_MODE:
        return render_template("private.html", app_name=APP_NAME)
    return render_template("index.html", app_name=APP_NAME)

@app.route("/login")
def login():
    # placeholder; em breve Google/Email/Shopify
    return redirect(url_for('home'))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", app_name=APP_NAME)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

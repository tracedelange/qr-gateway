from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def main():

    print("Gateway reached, redirecting to dbdruid")
    # log visit with google analytics

    return render_template('layout.html')
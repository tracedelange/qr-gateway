from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def main():

    print("Gateway reached, redirecting to dbdruid")

    return render_template('layout.html')
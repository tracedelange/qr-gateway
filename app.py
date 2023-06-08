from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def main():

    print("Gateway reached, redirecting to dbdruid")
    # log visit with google analytics
    # redirect to reubeen.dbdruid.com


    return redirect("https://reubeen.dbdruid.com", code=308)
from flask import Flask, request, render_template, session, redirect
import os
import random

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/")
def landing_page():
    session['maxGuess'] = 2
    if('randomNumber' not in session):
        session['guessCount'] = 0
        session['randomNumber'] = random.randint(1, 100)

    # print(myNum)
    return render_template("index.html")


@app.route("/guess", methods=['POST', 'GET'])
def guess():
    session['guessCount'] += 1
    session['guessNumber'] = int(request.form['aNumber'])
    return redirect("/")


@app.route("/reset")
def reset_count():
    session.pop('randomNumber')
    session.pop('guessNumber')
    return redirect("/")


@app.route("/tryagain")
def reset_guess():
    session.pop('guessNumber')
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

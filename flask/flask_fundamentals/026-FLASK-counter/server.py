from flask import Flask, request, redirect, render_template, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route("/")
def home():
    if('count' not in session):
        session['count'] = 1
    else:
        session['count'] += 1

    if('addamount' in session):
        print("*"*25)
        print(session['count'])
        print("*"*25)
        print("-"*25)
        print(session['addamount'])
        print("-"*25)
        session['count'] += (int(session['addamount']) - 1)
        session.pop('addamount')

    return render_template("index.html", count=session['count'])


@app.route("/plus", methods=['GET', 'POST'])
def plus_two():
    if(request.form['addamount']):
        session['addamount'] = request.form['addamount']
        print("YAY!")
    else:
        session['addamount'] = 2
    return redirect("/")


@app.route("/reset")
def destroy_session():
    session.pop('count')
    return redirect("/")


if(__name__ == "__main__"):
    app.run(debug=True)

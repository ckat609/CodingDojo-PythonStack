from flask import Flask, request, render_template, session, redirect
import os
import random

app = Flask(__name__)
app.secret_key = random._urandom(16)
print(app.secret_key)


def switch_case(source):
    switcher = {
        'house': random.randint(2, 5),
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'casino': random.randint(-50, 50)
    }
    return switcher[source]


@app.route("/")
def landing_page():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template("index.html")


@app.route("/process_gold", methods=['POST'])
def process_gold():
    goldSource = request.form['source']
    goldAmount = switch_case(request.form['source'])

    session['gold'] += goldAmount

    if (goldAmount >= 0):
        activitiesContent = f"<p class='win'>{goldAmount} was earned from the {goldSource}</p>"
    else:
        activitiesContent = f"<p class='lost'>{abs(goldAmount)} was lost at the {goldSource}</p>"

    session['activities'].append(activitiesContent)
    session['activitiesAmount'] = len(session['activities'])
    print(session['activitiesAmount'])
    return redirect("/")


@app.route("/reset", methods=['POST'])
def reset_all():
    del session['gold']
    del session['activities']
    return redirect("/")


if(__name__ == "__main__"):
    app.run(debug=True)

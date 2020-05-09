from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    strawQuantity = int(request.form['strawberry'])
    raspQuantity = int(request.form['raspberry'])
    appleQuantity = int(request.form['apple'])
    fruitCount = int(strawQuantity+raspQuantity+appleQuantity)
    fname = request.form['first_name']
    lname = request.form['last_name']
    studentId = request.form['student_id']
    orderTS = datetime.now()
    print(fruitCount)
    return render_template("checkout.html", fname=fname, lname=lname, strawQuantity=strawQuantity, raspQuantity=raspQuantity, appleQuantity=appleQuantity, studentId=studentId, fruitCount=fruitCount, orderTS=orderTS)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)

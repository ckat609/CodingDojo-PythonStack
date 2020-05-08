from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def landing_page():
    return(render_template("index.html"))


@app.route("/process", methods=["POST"])
def process_info():
    print(request.form)
    # subfname = request.form["fname"]
    # sublname = request.form["lname"]
    # subemail = request.form["email"]
    # subdojo = request.form["dojo"]
    # subfavlang = request.form["favlang"]
    # sublove = request.form["love"]
    # subfavs = request.form["favs"]
    # sublecture = request.form["lecture"]
    # sublab = request.form["lab"]
    # sublunch = request.form["lunch"]
    return render_template("show.html", subfname=request.form["fname"], sublname=request.form["lname"], subemail=request.form["email"], subdojo=request.form["dojo"], subfavlang=request.form["favlang"], sublove=request.form["love"], subfavs=request.form['favs'])


if(__name__ == "__main__"):
    app.run(debug=True)

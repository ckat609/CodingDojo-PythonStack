from flask import Flask

app = Flask(__name__)


@app.route("/")
def landing_page():
    return "Hello World!"


@app.route("/dojo")
def dojo():
    return "Dojo!"


@app.route("/say/<something>")
def say_something(something):
    return f"Hi, {something}!"


@app.route("/repeat/<int:times>/<something>")
def repeat_n_times(times, something):
    return (f"<p>{something}</p>"*times)


@app.errorhandler(404)
def page_not_found(e):
    return f"Rab, if you're reading this... let me know!"


if(__name__ == "__main__"):
    app.run(debug=True)

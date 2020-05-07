from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing_page():
    return "Go <a href='/play/'>HERE</a> instead!"


@app.route("/play")
def play():
    return render_template("index.html", numBoxes=None)


@app.route("/play/<int:boxes>")
def play_count(boxes):
    return render_template("index.html", numBoxes=boxes)


@app.route("/play/<int:boxes>/<color>")
def play_count_color(boxes, color):
    strColor = f"style='background-color: {color}; border: 1px solid dark{color}'"
    return render_template("index.html", numBoxes=boxes, strColor=color)


@app.errorhandler(404)
def show_error_page(e):
    return "<h1>Dumbass!</h1>"


if(__name__ == "__main__"):
    app.run(host="127.0.0.1", port=5000, debug=True)

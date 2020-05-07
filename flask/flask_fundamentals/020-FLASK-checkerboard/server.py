from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def landing_page():
    x = 8
    y = 8
    color1 = None
    color2 = None
    return render_template("index.html", width=x, height=y, col1=color2, col2=color2)


@app.route("/<int:y>")
def eightByY(y):
    x = 8
    # y = 8
    color1 = None
    color2 = None
    return render_template("index.html", width=x, height=y, col1=color2, col2=color2)


@app.route("/<int:x>/<int:y>")
def xByY(x, y):
    color1 = None
    color2 = None
    return render_template("index.html", width=x, height=y, col1=color2, col2=color2)


@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def xByY_withColor(x, y, color1, color2):
    return render_template("index.html", width=x, height=y, col1=color1, col2=color2)


if(__name__ == "__main__"):
    app.run(debug=True)

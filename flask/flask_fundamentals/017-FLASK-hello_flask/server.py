from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/success')
def success():
    return "success!"


@app.route('/hello/<aName>')
def hello_name(aName):
    # print(aName)
    return f"Hello, {aName}!"


@app.route('/users/<username>/<id>')
def disp_userinfo(username, id):
    print(username)
    print(id)
    return f"Username: {username} - ID: {id}"


if __name__ == "__main__":
    app.run(debug=True)

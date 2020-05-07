from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


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

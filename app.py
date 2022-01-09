from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"

@app.route("/hello/<username>")
def hello2(username):
    return "<h1>Hello {}.</h1>".format(username)

@app.route("/add/<x>/<y>")
def add(x, y):
    return str(int(x) + int(y))

## /hello_get?username=Allen&userage=22
@app.route("/hello_get")
def hello_get():
    username = request.args.get("username")
    userage = request.args.get("userage")
    if username == None:
        return "Who are you?"
    elif userage == None:
        return "Hello {}.".format(username)
    else:
        return "Hello {}, you are {} years old.".format(username, userage)


@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    outStr = """
    <form action="/hello_post" method="POST">
        <label>What's your name?</label>
        <input name="username">
        <button>SUBMIT</button>
    </form>
    """

    method = request.method ## "GET" or "POST"
    if method == "POST":
        username = request.form.get("username")
        outStr += """
        <h1>Hello {}.</h1>
        """.format(username)

    return outStr

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
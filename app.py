from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Simple Flask App</h2>
    <form action="/greet" method="post">
        <label>Enter your name:</label><br><br>
        <input type="text" name="username" placeholder="Your name">
        <br><br>
        <input type="submit" value="Submit">
    </form>
    """

@app.route("/greet", methods=["POST"])
def greet():
    username = request.form["username"]
    return f"<h1>Hello, {username}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>WWW-web</h1>
    <p>Hello from Render!!!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

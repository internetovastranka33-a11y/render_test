from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Cloud Computing - PaaS Demo</h1>
    <h2>Faculty of Management, Comenius University</h2>

    <p>This application is running in the cloud.</p>
    <p>Current server time: {datetime.now()}</p>

    <hr>

    <p>Version 2.0</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

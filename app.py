from flask import Flask, request, redirect

app = Flask(__name__)

votes = {
    "AWS": 0,
    "Azure": 0,
    "Google Cloud": 0,
    "None": 0
}

@app.route("/")
def home():
    total = sum(votes.values())

    results = ""
    for cloud, count in votes.items():
        percent = round((count / total * 100), 1) if total > 0 else 0

        results += f"""
        <div style="margin-bottom:15px">
            <b>{cloud}</b>: {count} hlasov ({percent}%)
            <div style="background:#ddd;width:100%;height:20px">
                <div style="
                    background:#4285f4;
                    width:{percent}%;
                    height:20px">
                </div>
            </div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Voting App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body style="
        font-family:Arial;
        max-width:700px;
        margin:50px auto;
        padding:20px;
    ">

        <h1>☁️ Cloud Computing – Live Poll</h1>

        <h2>Which cloud platform do you use most?</h2>

        <form method="POST" action="/vote">

            <button name="cloud" value="AWS">AWS</button>
            <button name="cloud" value="Azure">Azure</button>
            <button name="cloud" value="Google Cloud">Google Cloud</button>
            <button name="cloud" value="None">None</button>

        </form>

        <hr style="margin:30px 0">

        <h2>Live results</h2>

        {results}

        <p><b>Total votes:</b> {total}</p>

        <p style="color:#777">
            Running on Render PaaS
        </p>

    </body>
    </html>
    """


@app.route("/vote", methods=["POST"])
def vote():

    cloud = request.form.get("cloud")

    if cloud in votes:
        votes[cloud] += 1

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

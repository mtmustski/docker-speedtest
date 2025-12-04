from flask import Flask, render_template, jsonify

from app.speedtest import run_speedtest

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the main web interface."""
    return render_template("index.html")


@app.route("/api/speedtest", methods=["POST"])
def api_speedtest():
    """Run a speed test and return JSON results."""
    result = run_speedtest()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8012)

import os
from flask import Flask, request, jsonify, abort

app = Flask(__name__)
API_KEY = os.environ.get("MCP_API_KEY", "secret-key")

@app.route("/ping")
def ping():
    key = request.headers.get("X-API-Key")
    if key != API_KEY:
        abort(401)
    return jsonify({"message": "pong"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

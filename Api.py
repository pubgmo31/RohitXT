from flask import Flask, request, jsonify
import psutil
import platform
import time

app = Flask(__name__)

API_TOKEN = "MY_SECURE_TOKEN"

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "server": platform.node(),
        "system": platform.system()
    })

@app.route("/status")
def status():
    token = request.args.get("token")

    if token != API_TOKEN:
        return jsonify({
            "status": "error",
            "message": "Unauthorized"
        }), 403

    return jsonify({
        "status": "success",
        "cpu": psutil.cpu_percent(),
        "ram": psutil.virtual_memory().percent,
        "uptime": time.time()
    })

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")

    return jsonify({
        "status": "success",
        "message": f"Ping request received for {host}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
  

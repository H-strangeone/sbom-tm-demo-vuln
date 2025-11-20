from flask import Flask, request
import yaml
import requests

app = Flask(__name__)

@app.route("/unsafe_yaml", methods=["POST"])
def unsafe_yaml():
    # Vulnerable to YAML deserialization attack
    data = yaml.load(request.data, Loader=yaml.Loader)
    return {"loaded": str(data)}

@app.route("/")
def index():
    return "Hello from vulnerable demo!"

if __name__ == "__main__":
    app.run(debug=True)
print("Starting vulnerable Flask app...ss")
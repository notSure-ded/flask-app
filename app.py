from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app deployed using Jenkins + ArgoCD + AKS"

@app.route("/hello")
def hello():
    return "pipeline works"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
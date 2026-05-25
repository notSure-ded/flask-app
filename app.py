from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app deployed using Jenkins + ArgoCD + AKS"

@app.route("/hello")
def hello():
    return "pipeline works"

@app.route("/hell")
def hell():
    return "devops test"

app.route("/new-path")
def new_path():
    return "This is a new path added to the Flask app"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
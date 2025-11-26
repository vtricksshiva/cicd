from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! GitHub Actions deployed this Flask app on EC2 🎉"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


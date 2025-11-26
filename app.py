from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Deployed using GitHub Actions + EC2 with systemd!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


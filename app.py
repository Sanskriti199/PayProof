from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend setup and environment ready"

if __name__ == "__main__":
    app.run(debug=True)

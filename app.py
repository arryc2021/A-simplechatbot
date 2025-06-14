from flask import Flask, render_template, request
from agent import ask_agent

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        query = request.form["query"]
        response = ask_agent(query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

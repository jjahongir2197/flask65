from flask import Flask, render_template, request, redirect

app = Flask(__name__)

votes = {
    "Python": 0,
    "Java": 0,
    "C++": 0
}

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        choice = request.form["choice"]
        votes[choice] += 1

        return redirect("/")

    return render_template("index.html", votes=votes)

if __name__ == "__main__":
    app.run(debug=True)

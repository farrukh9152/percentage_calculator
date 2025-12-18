from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    percentage = None
    if request.method == "POST":
        obtained = float(request.form["obtained"])
        total = float(request.form["total"])
        percentage = (obtained / total) * 100
    return render_template("index.html", percentage=percentage)

if __name__ == "__main__":
    app.run(debug=True)

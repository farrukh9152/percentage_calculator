from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        subjects = ["Maths", "Science", "English", "Computer", "Hindi"]
        marks = []
        total = 0

        for sub in subjects:
            mark = int(request.form.get(sub))
            marks.append(mark)
            total += mark

        percentage = total / (len(subjects) * 100) * 100

        result = {
            "subjects": zip(subjects, marks),
            "total": total,
            "percentage": round(percentage, 2)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

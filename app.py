from flask import Flask, render_template, request, redirect

from database import get_complete_resume, save_resume

app = Flask(__name__)


@app.route("/")
def home():
    return "Resume Builder is running"

@app.route("/create", methods=["GET", "POST"])
def create_resume():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        date_of_birth = request.form["date_of_birth"]
        phone_number = request.form["phone_number"]
        location = request.form["location"]
        summary = request.form["summary"]
        school = request.form["school"]
        degree = request.form["degree"]
        field = request.form["field"]
        start_year = request.form["start_year"]
        end_year = request.form["end_year"]
        

        resume_id = save_resume(
            name,
            date_of_birth,
            email,
            phone_number,
            location,
            summary
        )
        save_education(
                resume_id,
                school,
                degree,
                field,
                start_year,
                end_year

            )
        
        return redirect(f"/resume/{resume_id}")
        return render_template("create_resume.html")
    


@app.route("/resume/<resume_id>")
def view_resume(resume_id):
    resume = get_complete_resume(int(resume_id))

    if resume is None:
        return "Resume not found."

    return render_template(
        "resume.html",
        resume=resume
    )


if __name__ == "__main__":
    app.run(debug=True)
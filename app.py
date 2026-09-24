from flask import Flask, render_template, request, redirect

from database import (
get_complete_resume, 
save_resume, 
save_education, 
save_work_experience,
save_skill,
save_certification
)
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

        job_title = request.form["job_title"]
        company = request.form["company"]
        location = request.form["location"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        description = request.form["description"]

        skill_1 = request.form["skill_1"]
        skill_2 = request.form["skill_2"]
        skill_3 = request.form["skill_3"]

        certification_name = request.form["certification_name"]
        certification_organization = request.form["certification_organization"]
        certification_date = request.form["certification_date"]
        

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
        save_work_experience(
            resume_id,
            job_title,
            company,
            location,
            start_date,
            end_date,
            description
        )
        save_skill(
            save_skill(resume_id, skill_1),
            save_skill(resume_id, skill_2),
            save_skill(resume_id, skill_3)
        )
        save_certification(
            resume_id,
            certification_name,
            certification_organization,
            certification_date
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
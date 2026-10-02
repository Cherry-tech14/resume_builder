from flask import Flask, render_template, request, redirect

from database import (
    get_complete_resume,
    save_resume,
    save_user,
    save_education,
    save_work_experience,
    save_skill,
    save_certification,
    save_project,
    save_language,
    save_achievement,
    save_volunteer_experience,
    save_reference,
    
    update_personal_information,
    update_summary,
    update_education,
    update_work_experience,
    update_skill,
    update_certification,
    update_project,
    update_language,
    update_achievement,
    update_volunteer_experience,
    update_reference
)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


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
        work_location = request.form["work_location"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        description = request.form["description"]

        
        skill_1 = request.form["skill_1"]
        skill_2 = request.form["skill_2"]
        skill_3 = request.form["skill_3"]


        certification_name = request.form["certification_name"]
        certification_organization = request.form[
            "certification_organization"
        ]
        certification_date = request.form["certification_date"]

        
        project_name = request.form.get("project_name")
        project_description = request.form.get("project_description")
        project_role = request.form.get("project_role")
        project_tools = request.form.get("project_tools")
        project_link = request.form.get("project_link")

        
        language = request.form["language"]
        language_proficiency = request.form["language_proficiency"]

    
        achievement_title = request.form["achievement_title"]
        achievement_description = request.form["achievement_description"]

        
        volunteer_organization = request.form["volunteer_organization"]
        volunteer_role = request.form["volunteer_role"]
        volunteer_location = request.form["volunteer_location"]
        volunteer_start_date = request.form["volunteer_start_date"]
        volunteer_end_date = request.form["volunteer_end_date"]
        volunteer_description = request.form["volunteer_description"]


        reference_name = request.form["reference_name"]
        reference_relationship = request.form["reference_relationship"]
        reference_organization = request.form["reference_organization"]
        reference_email = request.form["reference_email"]
        reference_phone_number = request.form["reference_phone_number"]

        
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
            work_location,
            start_date,
            end_date,
            description
        )

        
        save_skill(resume_id, skill_1)
        save_skill(resume_id, skill_2)
        save_skill(resume_id, skill_3)

        
        save_certification(
            resume_id,
            certification_name,
            certification_organization,
            certification_date
        )

        
        save_project(
            resume_id,
            project_name,
            project_description,
            project_role,
            project_tools,
            project_link
        )

    
        save_language(
            resume_id,
            language,
            language_proficiency
        )


        save_achievement(
            resume_id,
            achievement_title,
            achievement_description
        )

        
        save_volunteer_experience(
            resume_id,
            volunteer_organization,
            volunteer_role,
            volunteer_location,
            volunteer_start_date,
            volunteer_end_date,
            volunteer_description
        )

        
        save_reference(
            resume_id,
            reference_name,
            reference_relationship,
            reference_organization,
            reference_email,
            reference_phone_number
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


@app.route("/resume")
def find_resume():
    resume_id = request.args.get("resume_id")

    return redirect(f"/resume/{resume_id}")

@app.route("/edit/<resume_id>", methods=["GET", "POST"])
def edit_resume(resume_id):

    resume = get_complete_resume(int(resume_id))

    if resume is None:
        return "Resume not found."

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        date_of_birth = request.form["date_of_birth"]
        phone_number = request.form["phone_number"]
        location = request.form["location"]

        update_personal_information(
            int(resume_id),
            name,
            date_of_birth,
            email,
            phone_number,
            location
        )

        summary = request.form["summary"]

        update_summary(
            int(resume_id),
            summary
        )

        for education in resume["education"]:

            education_id = education["id"]

            school = request.form[f"school_{education_id}"]
            degree = request.form[f"degree_{education_id}"]
            field = request.form[f"field_{education_id}"]
            start_year = request.form[f"start_year_{education_id}"]
            end_year = request.form[f"end_year_{education_id}"]

            update_education(
                education_id,
                school,
                degree,
                field,
                start_year,
                end_year
            )
        for experience in resume["work_experience"]:
            experience_id = experience["id"]

            job_title = request.form[f"job_title_{experience_id}"]
            company = request.form[f"company_{experience_id}"]
            work_location = request.form[f"work_location_{experience_id}"]
            start_date = request.form[f"start_date_{experience_id}"]
            end_date = request.form[f"end_date_{experience_id}"]
            description = request.form[f"description_{experience_id}"]

            update_work_experience(
                experience_id,
                job_title,
                company,
                work_location,
                start_date,
                end_date,
                description
            )

        for skill in resume["skills"]:
            skill_id = skill["id"]
            skill_value = request.form[f"skill_{skill_id}"]

            update_skill(
                skill_id,
                skill_value
            )
        new_skill = request.form["new_skill"]
        if new_skill:
            save_skill(
                int(resume_id),
                new_skill
            )

        for certification in resume["certifications"]:

            certification_id = certification["id"]

            name = request.form[
                f"certification_name_{certification_id}"
            ]  

            organization = request.form[
                f"certification_organization_{certification_id}"
            ]

            date = request.form[
                f"certification_date_{certification_id}"
            ]

            update_certification(
                certification_id,
                name,
                organization,
                date
            )

        
        for project in resume["projects"]:

            project_id = project["id"]

            project_name = request.form[
                f"project_name_{project_id}"
            ]

            project_description = request.form[
                f"project_description_{project_id}"
            ]

            project_role = request.form[
                f"project_role_{project_id}"
            ]

            project_tools = request.form[
                f"project_tools_{project_id}"
            ]

            project_link = request.form[
                f"project_link_{project_id}"
            ]

            update_project(
                project_id,
                project_name,
                project_description,
                project_role,
                project_tools,
                project_link
            )

        for language in  resume["languages"]:
            language_id = language["id"]
            language_name = request.form[
                f"language_{language_id}"
            ]
            proficiency = request.form[
                f"language_proficiency_{language_id}"
            ]

            update_language(
                language_id,
                language_name,
                proficiency
            )

        for achievement in resume["achievements"]:
            achievement_id = achievement["id"]

            title = request.form[
                f"achievement_title_{achievement_id}"
            ]

            description = request.form[
                f"achievement_description_{achievement_id}"
            ]
            update_achievement(
                achievement_id,
                title,
                description
            )

        for volunteer in resume["volunteer_experience"]:

            volunteer_id = volunteer["id"]

            organization = request.form[
                f"volunteer_organization_{volunteer_id}"
            ]

            role = request.form[
                f"volunteer_role_{volunteer_id}"
            ]

            location = request.form[
                f"volunteer_location_{volunteer_id}"
            ]

            start_date = request.form[
                f"volunteer_start_date_{volunteer_id}"
            ]

            end_date = request.form[
                f"volunteer_end_date_{volunteer_id}"
            ]

            description = request.form[
                f"volunteer_description_{volunteer_id}"
            ]

            update_volunteer_experience(
                volunteer_id,
                organization,
                role,
                location,
                start_date,
                end_date,
                description
            )

        for reference in resume["references"]:

            reference_id = reference["id"]

            name = request.form[
                f"reference_name_{reference_id}"
            ]

            relationship = request.form[
                f"reference_relationship_{reference_id}"
            ]

            organization = request.form[
                f"reference_organization_{reference_id}"
            ]

            email = request.form[
                f"reference_email_{reference_id}"
            ]

            phone_number = request.form[
                f"reference_phone_number_{reference_id}"
            ]
            
            update_reference(
                reference_id,
                name,
                relationship,
                organization,
                email,
                phone_number
    )


        return redirect(f"/resume/{resume_id}")

    return render_template(
        "edit_resume.html",
        resume=resume
    )

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        save_user(name, email)

        return redirect("/")

    return render_template("register.html")
    
if __name__ == "__main__":
    app.run(debug=True)
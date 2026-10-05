from flask import Flask, render_template, request, redirect

from database import (
    get_complete_resume,
    save_resume,
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

        schools = request.form.getlist("school")
        degrees = request.form.getlist("degree")
        fields = request.form.getlist("field")
        start_years = request.form.getlist("start_year")
        end_years = request.form.getlist("end_year")

        
        job_titles = request.form.getlist("job_title")
        companies = request.form.getlist("company")
        work_locations = request.form.getlist("work_location")
        start_dates = request.form.getlist("start_date")
        end_dates = request.form.getlist("end_date")
        descriptions = request.form.getlist("description")

        skills = request.form.getlist("skill")
       

        certification_names = request.form.getlist("certification_name")
        certification_organizations = request.form.getlist("certification_organization")
        certification_dates = request.form.getlist("certification_date")

        
        project_names = request.form.getlist("project_name")
        project_descriptions = request.form.getlist("project_description")
        project_roles = request.form.getlist("project_role")
        project_tools_list = request.form.getlist("project_tools")
        project_links = request.form.getlist("project_link")

        
        languages = request.form.getlist("language")
        language_proficiencies = request.form.getlist("language_proficiency")

    
        achievement_titles = request.form.getlist("achievement_title")
        achievement_descriptions = request.form.getlist(
            "achievement_description"
        )

        
        volunteer_organizations = request.form.getlist("volunteer_organization")
        volunteer_roles = request.form.getlist("volunteer_role")
        volunteer_locations = request.form.getlist("volunteer_location")
        volunteer_start_dates = request.form.getlist("volunteer_start_date")
        volunteer_end_dates = request.form.getlist("volunteer_end_date")
        volunteer_descriptions = request.form.getlist("volunteer_description")

    
        reference_names = request.form.getlist("reference_name")
        reference_relationships = request.form.getlsit("reference_relationship")
        reference_organizations = request.form.getlist("reference_organization")
        reference_emails = request.form.getlist("reference_email")
        reference_phone_numbers = request.form.getlist("reference_phone_number")

    
        resume_id = save_resume(
            name,
            date_of_birth,
            email,
            phone_number,
            location,
            summary
        )

    
        for school, degree, field, start_year, end_year in zip(
            schools,
            degrees,
            fields,
            start_years,
            end_years
        ):
            if school or degree or field or start_year or end_year:
                save_education(
                    resume_id,
                    school,
                    degree,
                    field,
                    start_year,
                    end_year
                )

        
        for (
            job_title,
            company,
            work_location,
            start_date,
            end_date,
            description
        ) in zip(
            job_titles,
            companies,
            work_locations,
            start_dates,
            end_dates,
            descriptions
        ):
            if (
                job_title
                or company
                or work_location
                or start_date
                or end_date
                or description
        ):
                save_work_experience(
                    resume_id,
                    job_title,
                    company,
                    work_location,
                    start_date,
                    end_date,
                   description
                )  

        
        for skill in skills:
            if skill:
                save_skill(resume_id, skill)

        
        for (
            name,
            organization,
            date,
        ) in zip(
            certification_names,
            certification_organizations,
            certification_dates

        ):
            if name or organization or date:
                save_certification(
                    resume_id,
                    name,
                    organization,
                    date
            )

        
        for (
            project_name,
            project_description,
            project_role,
            project_tools,
            project_link
        ) in zip(
            project_names,
            project_descriptions,
            project_roles,
            project_tools_list,
            project_links
        ):
            if (
                project_name
                or project_description
                or project_role
                or project_tools
                or project_link
            ):
                save_project(
                    resume_id,
                    project_name,
                    project_description,
                    project_role,
                    project_tools,
                    project_link
                )

        
        for language, proficiency in zip(
            languages,
            language_proficiencies
        ):
            if language or proficiency:
                save_language(
                    resume_id,
                    language,
                    proficiency
                )


        for title, description in zip(
            achievement_titles,
            achievement_descriptions
        ):
            if title or description:
                save_achievement(
                    resume_id,
                    title,
                    description
                )

        
        for (
            organization,
            role,
            location,
            start_date,
            end_date,
            description
        ) in zip(
            volunteer_organizations,
            volunteer_roles,
            volunteer_locations,
            volunteer_start_dates,
            volunteer_end_dates,
            volunteer_descriptions
        ):
            if (
                organization
                or role
                or location
                or start_date
                or end_date
                or description

            ):
                save_volunteer_experience(
                    resume_id,
                    organization,
                    role,
                    location,
                    start_date,
                    end_date,
                    description
            )

        for (
            name,
            relationship,
            organization,
            email,
            phone_number
        ) in zip(
            reference_names,
            reference_relationships,
            reference_organizations,
            reference_emails,
            reference_phone_numbers

        ):
            if (
                name
                or relationship
                or organization
                or email
                or phone_number
            ):
                save_reference(
                    resume_id,
                    name,
                    relationship,
                    organization,
                    email,
                    phone_number
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
        date_of_birth = request.form["date_of_birth"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        location = request.form["location"]

        update_personal_information(
            resume_id,
            name,
            date_of_birth,
            email,
            phone_number,
            location
        )


        summary = request.form["summary"]

        update_summary(
            resume_id,
            summary
        )

      
        for education in resume["education"]:

            education_id = education["id"]

            school = request.form.get(
                f"school_{education_id}"
            )

            degree = request.form.get(
                f"degree_{education_id}"
            )

            field = request.form.get(
                f"field_{education_id}"
            )

            start_year = request.form.get(
                f"start_year_{education_id}"
            )

            end_year = request.form.get(
                f"end_year_{education_id}"
            )

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

            job_title = request.form.get(
                f"job_title_{experience_id}"
            )

            company = request.form.get(
                f"company_{experience_id}"
            )

            work_location = request.form.get(
                f"work_location_{experience_id}"
            )

            start_date = request.form.get(
                f"start_date_{experience_id}"
            )

            end_date = request.form.get(
                f"end_date_{experience_id}"
            )

            description = request.form.get(
                f"description_{experience_id}"
            )

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

            skill_value = request.form.get(
                f"skill_{skill_id}"
            )

            update_skill(
                skill_id,
                skill_value
            )


        for certification in resume["certifications"]:

            certification_id = certification["id"]

            name = request.form.get(
                f"certification_name_{certification_id}"
            )

            organization = request.form.get(
                f"certification_organization_{certification_id}"
            )

            date = request.form.get(
                f"certification_date_{certification_id}"
            )

            update_certification(
                certification_id,
                name,
                organization,
                date
            )


        for project in resume["projects"]:

            project_id = project["id"]

            project_name = request.form.get(
                f"project_name_{project_id}"
            )

            project_description = request.form.get(
                f"project_description_{project_id}"
            )

            project_role = request.form.get(
                f"project_role_{project_id}"
            )

            project_tools = request.form.get(
                f"project_tools_{project_id}"
            )

            project_link = request.form.get(
                f"project_link_{project_id}"
            )

            update_project(
                project_id,
                project_name,
                project_description,
                project_role,
                project_tools,
                project_link
            )


        for language in resume["languages"]:

            language_id = language["id"]

            language_value = request.form.get(
                f"language_{language_id}"
            )

            proficiency = request.form.get(
                f"language_proficiency_{language_id}"
            )

            update_language(
                language_id,
                language_value,
                proficiency
            )

        for achievement in resume["achievements"]:

            achievement_id = achievement["id"]

            title = request.form.get(
                f"achievement_title_{achievement_id}"
            )

            description = request.form.get(
                f"achievement_description_{achievement_id}"
            )

            update_achievement(
                achievement_id,
                title,
                description
            )

        for volunteer in resume["volunteer_experience"]:

            volunteer_id = volunteer["id"]

            organization = request.form.get(
                f"volunteer_organization_{volunteer_id}"
            )

            role = request.form.get(
                f"volunteer_role_{volunteer_id}"
            )

            location = request.form.get(
                f"volunteer_location_{volunteer_id}"
            )

            start_date = request.form.get(
                f"volunteer_start_date_{volunteer_id}"
            )

            end_date = request.form.get(
                f"volunteer_end_date_{volunteer_id}"
            )

            description = request.form.get(
                f"volunteer_description_{volunteer_id}"
            )

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

            name = request.form.get(
                f"reference_name_{reference_id}"
            )

            relationship = request.form.get(
                f"reference_relationship_{reference_id}"
            )

            organization = request.form.get(
                f"reference_organization_{reference_id}"
            )

            email = request.form.get(
                f"reference_email_{reference_id}"
            )

            phone_number = request.form.get(
                f"reference_phone_number_{reference_id}"
            )

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

if __name__ == "__main__":
    app.run(debug=True)
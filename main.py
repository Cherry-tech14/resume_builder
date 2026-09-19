from resume_data import (
    get_personal_information,
    get_summary,
    get_education,
    get_work_experience,
    get_skills,
    get_certifications,
    get_projects,
    get_languages,
    get_achievements,
    get_volunteer,
    get_references
)

from storage import save_resume, load_resume

from database import (
    save_resume as save_resume_to_database,
    save_education,
    save_work_experience,
    save_skill,
    save_certification,
    save_project,
    save_language,
    save_achievement,
    save_volunteer_experience,
    save_reference,
    get_complete_resume
)
from display import (
    display_education,
    display_skills,
    display_work_experience,
    display_certifications,
    display_projects,
    display_languages,
    display_achievements,
    display_volunteer,
    display_references,
    
)

from edit_resume import edit_resume


def main():
    saved_resume = load_resume()

    if saved_resume:
        print("A saved resume was found.")

        while True:
            print("1. Create a new resume")
            print("2. Load existing resume")
            print("3. Edit existing resume")

            choice = input("Enter your choice: ")

            if choice in ("1", "2", "3"):
                break

            print("Invalid choice. Please enter 1, 2, or 3.")

        if choice == "1":
            print("Creating a new resume.")

        elif choice == "2":
            print("Loading existing resume.")
            resume_id = int(input("Enter the resume ID: "))
            resume = get_complete_resume(resume_id)

            if resume is None:
                print("Resume not found.")
                return

            personal_information = saved_resume["personal_information"]

            print("\nRESUME INFORMATION")
            print("Name:", personal_information["name"])
            print("Date of Birth:", personal_information["date_of_birth"])
            print("Email:", personal_information["email"])
            print("Phone Number:", personal_information["phone_number"])
            print("Location:", personal_information["location"])

            print("\nPROFESSIONAL SUMMARY")
            print("Summary:", saved_resume["summary"])

            display_education(saved_resume["education"])
            display_skills(saved_resume["skills"])
            display_work_experience(saved_resume["work_experience"])
            display_certifications(saved_resume["certifications"])
            display_projects(saved_resume["projects"])
            display_languages(saved_resume["languages"])
            display_achievements(saved_resume["achievements"])
            display_volunteer(saved_resume["volunteer_experience"])
            display_references(saved_resume["references"])

            return

        elif choice == "3":
            resume_id = int(input("Enter the resume ID: "))
            saved_resume = get_complete_resume(resume_id)
            if saved_resume is None:
                print("Resume not found.")
                return
            edit_resume(saved_resume)
            

            return

    else:
        print("No saved resume found.")

    print("\nRESUME BUILDER")
    print("Welcome! Let's create your professional resume.")

    name, date_of_birth, email, phone_number, location = get_personal_information()

    summary = get_summary()


    resume_id = save_resume_to_database(
        name,
        date_of_birth,
        email,
        phone_number,
        location,
        summary
    )

    educations = get_education()
    for education in educations:
        save_education(
            resume_id,
            education["school"],
            education["degree"],
            education["field"],
            education["start_year"],
            education["end_year"]
        )

    work_experiences = get_work_experience()
    for experience in work_experiences:
        resume_id,
        experience["job_title"],
        experience["company"],
        experience["location"],
        experience["start_date"],
        experience["end_date"],
        experience["description"]

    skills = get_skills()
    for skill in skills:
        save_skill(
            resume_id,
            skill
        )

    certifications = get_certifications()
    for certification in certifications:
        save_certification(
        resume_id,
        certification["name"],
        certification["organization"],
        certification["date"]

        )
        
    projects = get_projects()
    for project in projects:
        save_project(
            resume_id,
            project["project-name"],
            project["description"],
            project["role"],
            project["tools"],
            project["project_link"]

        )
    languages = get_languages()
    for language in languages:
        save_language(
            resume_id,
            language["language"],
            language["proficiency"]
        )

    achievements = get_achievements()
    for achievement in achievements:
        save_achievement(
            resume_id,
            achievement["title"],
            achievement["description"]
        )

    volunteer_experiences = get_volunteer()
    for volunteer in volunteer_experiences:
        save_volunteer_experience(
            resume_id,
            volunteer["organization"],
            volunteer["role"],
            volunteer["location"],
            volunteer["start_date"],
            volunteer["end_date"],
            volunteer["description"]
        )
    
    references = get_references()
    for reference in references:
        save_reference(
            resume_id,
            reference["name"],
            reference["relationship"],
            reference["organization"],
            reference["email"],
            reference["phone_number"]
    )
        

    resume = {
        "personal_information": {
            "name": name,
            "date_of_birth": date_of_birth,
            "email": email,
            "phone_number": phone_number,
            "location": location
        },
        "summary": summary,
        "education": educations,
        "work_experience": work_experiences,
        "skills": skills,
        "certifications": certifications,
        "projects": projects,
        "languages": languages,
        "achievements": achievements,
        "volunteer_experience": volunteer_experiences,
        "references": references
    }

    save_resume(resume)

    print("\nResume saved to SQLite with ID:", resume_id)

    print("\nRESUME INFORMATION")
    print("Name:", name)
    print("Date of Birth:", date_of_birth)
    print("Email:", email)
    print("Phone Number:", phone_number)
    print("Location:", location)

    print("\nPROFESSIONAL SUMMARY")
    print("Summary:", summary)

    display_education(educations)
    display_skills(skills)
    display_work_experience(work_experiences)
    display_certifications(certifications)
    display_projects(projects)
    display_languages(languages)
    display_achievements(achievements)
    display_volunteer(volunteer_experiences)
    display_references(references)


if __name__ == "__main__":
    main()

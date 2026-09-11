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

from display import (
    display_education,
    display_skills,
    display_work_experience,
    display_certifications,
    display_projects,
    display_languages,
    display_achievements,
    display_volunteer,
    display_references
)


def main():
    print("RESUME BUILDER")
    print("Welcome! Let's create your professional resume.")

    name, date_of_birth, email, phone_number, location = get_personal_information()
    summary = get_summary()
    educations = get_education()
    work_experiences = get_work_experience()
    skills = get_skills()
    certifications = get_certifications()
    projects = get_projects()
    languages = get_languages()
    achievements = get_achievements()
    volunteer_experiences = get_volunteer()
    references = get_references()

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
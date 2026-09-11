def display_education(educations):
    print("\nEDUCATION")

    for education in educations:
        print("School:", education["school"])
        print("Degree:", education["degree"])
        print("Field of Study:", education["field"])
        print("Start Year:", education["start_year"])
        print("End Year:", education["end_year"])
        print()


def display_skills(skills):
    print("\nSKILLS")

    for skill in skills:
        print("•", skill)


def display_work_experience(work_experiences):
    print("\nWORK EXPERIENCE")

    for experience in work_experiences:
        print("Job Title:", experience["job_title"])
        print("Company:", experience["company"])
        print("Location:", experience["location"])
        print("Start Date:", experience["start_date"])
        print("End Date:", experience["end_date"])
        print("Description:", experience["description"])
        print()


def display_certifications(certifications):
    print("\nCERTIFICATIONS")

    for certification in certifications:
        print("Name:", certification["name"])
        print("Organization:", certification["organization"])
        print("Date:", certification["date"])
        print()


def display_projects(projects):
    print("\nPROJECTS")

    for project in projects:
        print("Project Name:", project["project_name"])
        print("Description:", project["description"])
        print("Role:", project["role"])
        print("Tools/Technologies:", project["tools"])
        print("Project Link:", project["project_link"])
        print()


def display_languages(languages):
    print("\nLANGUAGES")

    for language in languages:
        print("Language:", language["language"])
        print("Proficiency:", language["proficiency"])
        print()


def display_achievements(achievements):
    print("\nACHIEVEMENTS")

    for achievement in achievements:
        print("Title:", achievement["title"])
        print("Description:", achievement["description"])
        print()


def display_volunteer(volunteer_experiences):
    print("\nVOLUNTEER EXPERIENCE")

    for volunteer in volunteer_experiences:
        print("Organization:", volunteer["organization"])
        print("Role:", volunteer["role"])
        print("Location:", volunteer["location"])
        print("Start Date:", volunteer["start_date"])
        print("End Date:", volunteer["end_date"])
        print("Description:", volunteer["description"])
        print()


def display_references(references):
    print("\nREFERENCES")

    for reference in references:
        print("Name:", reference["name"])
        print("Relationship:", reference["relationship"])
        print("Organization:", reference["organization"])
        print("Email:", reference["email"])
        print("Phone Number:", reference["phone_number"])
        print()
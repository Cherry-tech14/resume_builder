print("RESUME BUILDER")
print("Welcome! Let's create your professional resume.")


def get_personal_information():
    name = input("Enter your full name: ")
    date_of_birth = input("Enter your date of birth (optional): ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    location = input("Enter your location: ")

    return name, date_of_birth, email, phone_number, location


def get_summary():
    summary = ""
    summary = input("Enter your professional summary (optional): ")
    include_summary = input("Do you want to add a professional summary? (yes/no): ")
    if include_summary.lower() == "yes":
        summary = input("Enter your professional summary: ")
    return summary


def get_education():
    educations = []

    while True:
        school = input("Enter name of school: ")
        degree = input("Enter your degree or qualification(optional): ")
        field = input("Enter your field of study: ")
        start_year = input("Enter your start year: ")
        end_year = input("Enter your end year: ")

        education = {
            "school": school,
            "degree": degree,
            "field": field,
            "start_year": start_year,
            "end_year": end_year
        }

        educations.append(education)

        another = input("Do you want to add another education? (yes/no): ")

        if another.lower() != "yes":
            break

    return educations


def get_work_experience():
    experiences = []

    include_experience = input(
        "Do you want to add work experience? (yes/no): "
    )

    if include_experience.lower() == "yes":
        while True:
            job_title = input("Enter your job title: ")
            company = input("Enter the company name: ")
            location = input("Enter the job location: ")
            start_date = input("Enter your start date: ")
            end_date = input("Enter your end date (or present): ")
            description = input("Describe your responsibilities: ")

            experience = {
                "job_title": job_title,
                "company": company,
                "location": location,
                "start_date": start_date,
                "end_date": end_date,
                "description": description
            }

            experiences.append(experience)

            another = input(
                "Do you want to add another work experience? (yes/no): "
            )

            if another.lower() != "yes":
                break

    return experiences


def get_skills():
    skills = []

    while True:
        skill = input("Enter a skill: ")
        skills.append(skill)

        another = input("Do you want to add another skill? (yes/no): ")

        if another.lower() != "yes":
            break

    return skills


def get_certifications():
    certifications = []

    include_certifications = input(
        "Do you want to add certifications? (yes/no): "
    )

    if include_certifications.lower() == "yes":
        while True:
            name = input("Enter certification name: ")
            organization = input("Enter issuing organization: ")
            date = input("Enter date obtained: ")

            certification = {
                "name": name,
                "organization": organization,
                "date": date
            }

            certifications.append(certification)

            another = input(
                "Do you want to add another certification? (yes/no): "
            )

            if another.lower() != "yes":
                break

    return certifications

def get_projects():
    projects = []

    include_projects = input(
        "Do you want to add projects? (yes/no): "
    )

    if include_projects.lower() == "yes":
        while True:
            project_name = input("Enter project name: ")
            description = input("Describe the project: ")
            role = input("What was your role in the project? ")
            tools = input("What tools or technologies did you use? ")
            project_link = input("Enter project link (optional): ")

            project = {
                "project_name": project_name,
                "description": description,
                "role": role,
                "tools": tools,
                "project_link": project_link
            }

            projects.append(project)

            another = input(
                "Do you want to add another project? (yes/no): "
            )

            if another.lower() != "yes":
                break

    return projects
def get_language():
    languages = []
    include_languages = input("Do you want to add projects? (yes/no): ")

    while True:
        language = input("Enter language: ")
        proficiency = input("Enter your proficiency level: ")

        language_info = {
            "language": language,
            "proficiency": proficiency
        }
        languages.append(language_info)
        another = input("Do you want to add another language? (yes/no): ")
        if another.lower() != "yes":
            break
    return languages

def get_achievements():
    achievements = []

    include_achievements = input(
        "Do you want to add achievements? (yes/no): "
    )

    if include_achievements.lower() == "yes":
        while True:
            title = input("Enter achievement title: ")
            description = input("Describe the achievement: ")

            achievement = {
                "title": title,
                "description": description
            }

            achievements.append(achievement)

            another = input(
                "Do you want to add another achievement? (yes/no): "
            )

            if another.lower() != "yes":
                break

    return achievements
name, date_of_birth, email, phone_number, location = get_personal_information()
summary = get_summary()
educations = get_education()
work_experiences = get_work_experience()
skills = get_skills()
certifications = get_certifications()
projects = get_projects()
languages = get_language()
achievements = get_achievements()

print("\nRESUME INFORMATION")
print("Name:", name)
print("Date of Birth:", date_of_birth)
print("Email:", email)
print("Phone Number:", phone_number)
print("Location:", location)

print("\nPROFESSIONAL SUMMARY")

print("\nEDUCATION")
print(educations)

print("\nWORK EXPERIENCE")
print(work_experiences)

print("\nSKILLS")
print(skills)

print("\nCERTIFICATION")
print(certifications)

print("\nPROJECTS")
print(projects)

print("\nLANGUAGES")
print(languages)

print("\nACHIEVEMENTS")
print(achievements)
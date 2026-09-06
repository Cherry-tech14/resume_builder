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
    summary = input("Enter your professional summary: ")
    return summary


def get_education():
    educations = []

    while True:
        school = input("Enter name of school: ")
        degree = input("Enter your degree or qualification: ")
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

        another = input("Do you want to add another work experience? (yes/no): ")

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
    while True:
        name = input("Enter certification name: ")
        organization = input("Enter issuing organization: ")
        date = input("Enter date obtained: ")

        certification = {
            "name": name,
            "organization": organization,
            "date": date

        }
        another = input("Do you want to add another certification? (yes/no): ")
        if another.lower() != "yes":
            break


name, date_of_birth, email, phone_number, location = get_personal_information()
summary = get_summary()
educations = get_education()
work_experiences = get_work_experience()
skills = get_skills()
certifications = get_certifications()

print("\nRESUME INFORMATION")
print("Name:", name)
print("Email:", email)
print("Phone Number:", phone_number)
print("Location:", location)

print("\nPROFESSIONAL SUMMARY")
print("Summary:", summary)

print("\nEducation:")
print(educations)

print("\nWORK EXPERIENCE")
print(work_experiences)

print("\nSKILLS")
print(skills)

print("\n CERTIFICATION")
print(certifications)
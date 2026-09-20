from database import (
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

def edit_resume(saved_resume, resume_id):
    print("\nEDIT RESUME")

    print("1. Personal information")
    print("2. Professional summary")
    print("3. Education")
    print("4. Work experience")
    print("5. Skills")
    print("6. Certifications")
    print("7. Projects")
    print("8. Languages")
    print("9. Achievements")
    print("10. Volunteer experience")
    print("11. References")

    edit_choice = input("What would you like to edit? ")

    if edit_choice == "1":
        edit_personal_information(saved_resume, resume_id)

    elif edit_choice == "2":
        edit_summary(saved_resume, resume_id)

    elif edit_choice == "3":
        edit_education(saved_resume, resume_id)

    elif edit_choice == "4":
        edit_work_experience(saved_resume, resume_id)
    
    elif edit_choice == "5":
        edit_skills(saved_resume, resume_id)

    elif edit_choice == "6":
        edit_certifications(saved_resume, resume_id)

    elif edit_choice == "7":
        edit_projects(saved_resume, resume_id)

    elif edit_choice == "8":
        edit_languages(saved_resume, resume_id)
    
    elif edit_choice == "9":
        edit_achievements(saved_resume, resume_id)

    elif edit_choice == "10":
        edit_volunteer(saved_resume, resume_id)

    elif edit_choice == "11":
        edit_references(saved_resume, resume_id)

    else:
        print("That editing option has not been implemented yet.")


def edit_personal_information(saved_resume, resume_id):
    print("\nPERSONAL INFORMATION")

    print("1. Name")
    print("2. Date of Birth")
    print("3. Email")
    print("4. Phone Number")
    print("5. Location")

    personal_choice = input("What would you like to change? ")

    if personal_choice == "1":
        new_name = input("Enter your new name: ")
        saved_resume["personal_information"]["name"] = new_name

    elif personal_choice == "2":
        new_date_of_birth = input(
            "Enter your new date of birth: "
        )
        saved_resume["personal_information"]["date_of_birth"] = new_date_of_birth

    elif personal_choice == "3":
        new_email = input("Enter your new email: ")
        saved_resume["personal_information"]["email"] = new_email

    elif personal_choice == "4":
        new_phone_number = input(
            "Enter your new phone number: "
        )
        saved_resume["personal_information"]["phone_number"] = new_phone_number

    elif personal_choice == "5":
        new_location = input("Enter your new location: ")
        saved_resume["personal_information"]["location"] = new_location
    
    

    else:
        print("Invalid choice.")
        return
    personal_information = saved_resume["personal_information"]

    update_personal_information(
        resume_id,
        personal_information["name"],
        personal_information["date_of_birth"],
        personal_information["email"],
        personal_information["phone_number"],
        personal_information["location"]
    )

    print("Personal information updated successfully.")

def edit_summary(saved_resume, resume_id):
    new_summary = input(
        "Enter your new professional summary: "
    )

    saved_resume["summary"] = new_summary

    update_summary(
        resume_id,
        new_summary
    )

    print("Professional summary updated successfully.")

def edit_education(saved_resume, resume_id):
    educations = saved_resume["education"]

    if not educations:
        print("No education information found.")
        return

    print("\nEDUCATION")

    for index, education in enumerate(educations, start=1):
        print(
            index,
            education["school"],
            "-",
            education["degree"],
            "-",
            education["field"]
        )

    education_choice = input(
        "Enter the number of the education you want to edit: "
    )

    if not education_choice.isdigit():
        print("Invalid choice.")
        return

    education_index = int(education_choice) - 1

    if education_index < 0 or education_index >= len(educations):
        print("Invalid choice.")
        return

    print("\nWhat would you like to edit?")
    print("1. School")
    print("2. Degree")
    print("3. Field of study")
    print("4. Start year")
    print("5. End year")

    field_choice = input("Enter your choice: ")

    education = educations[education_index]
    education_id = education["id"]

    if field_choice == "1":
        education["school"] = input(
            "Enter the new school name: "
        )

    elif field_choice == "2":
        education["degree"] = input(
            "Enter the new degree or qualification: "
        )

    elif field_choice == "3":
        education["field"] = input(
            "Enter the new field of study: "
        )

    elif field_choice == "4":
        education["start_year"] = input(
            "Enter the new start year: "
        )

    elif field_choice == "5":
        education["end_year"] = input(
            "Enter the new end year: "
        )

    else:
        print("Invalid choice.")
        return

    update_education(
        education_id,
        education["school"],
        education["degree"],
        education["field"],
        education["start_year"],
        education["end_year"]
    )

    print("Education updated successfully.")

def edit_work_experience(saved_resume, resume_id):
    experiences = saved_resume["work_experience"]

    if not experiences:
        print("No work experience found.")
        return

    print("\nWORK EXPERIENCE")

    for index, experience in enumerate(experiences, start=1):
        print(
            index,
            experience["job_title"],
            "-",
            experience["company"]
        )

    experience_choice = input(
        "Enter the number of the work experience you want to edit: "
    )

    if not experience_choice.isdigit():
        print("Invalid choice.")
        return

    experience_index = int(experience_choice) - 1

    if experience_index < 0 or experience_index >= len(experiences):
        print("Invalid choice.")
        return

    print("\nWhat would you like to edit?")
    print("1. Job title")
    print("2. Company")
    print("3. Location")
    print("4. Start date")
    print("5. End date")
    print("6. Description")

    field_choice = input("Enter your choice: ")

    experience = experiences[experience_index]
    work_id = experience["id"]

    if field_choice == "1":
        experience["job_title"] = input(
            "Enter the new job title: "
        )

    elif field_choice == "2":
        experience["company"] = input(
            "Enter the new company name: "
        )

    elif field_choice == "3":
        experience["location"] = input(
            "Enter the new location: "
        )

    elif field_choice == "4":
        experience["start_date"] = input(
            "Enter the new start date: "
        )

    elif field_choice == "5":
        experience["end_date"] = input(
            "Enter the new end date: "
        )

    elif field_choice == "6":
        experience["description"] = input(
            "Enter the new description: "
        )

    else:
        print("Invalid choice.")
        return
    
    update_work_experience(
        work_id,
        experience["job_title"],
        experience["company"],
        experience["location"],
        experience["start_date"],
        experience["end_date"],
        experience["description"]
)
    print("Work experience updated successfully.")

def edit_skills(saved_resume, resume_id):
    skills = saved_resume["skills"]

    if not skills:
        print("No skills found.")
        return

    while True:
        print("\nSKILLS")

        for index, skill in enumerate(skills, start=1):
            print(index, skill["skill"])

        skill_choice = input(
            "Enter the number of the skill you want to edit: "
        )

        if not skill_choice.isdigit():
            print("Invalid choice.")
            continue

        skill_index = int(skill_choice) - 1

        if skill_index < 0 or skill_index >= len(skills):
            print("Invalid choice.")
            continue

        new_skill = input("Enter the new skill: ")

        skills= skills[skill_index]
        skill_id = skill["id"]

        skill["skill"] = new_skill

        update_skill(
            skill_id,
            skill["skill"]
        )

        print("Skill updated successfully.")

        another = input(
            "Do you want to edit another skill? (yes/no): "
        )

        if another.lower() != "yes":
            break

def edit_certifications(saved_resume, resume_id):
    certifications = saved_resume["certifications"]

    if not certifications:
        print("No certifications found.")
        return

    while True:
        print("\nCERTIFICATIONS")

        for index, certification in enumerate(certifications, start=1):
            print(
                index,
                certification["name"],
                "-",
                certification["organization"]
            )

        certification_choice = input(
            "Enter the number of the certification you want to edit: "
        )

        if not certification_choice.isdigit():
            print("Invalid choice.")
            continue

        certification_index = int(certification_choice) - 1

        if (
            certification_index < 0
            or certification_index >= len(certifications)
        ):
            print("Invalid choice.")
            continue

        print("\nWhat would you like to edit?")
        print("1. Certification name")
        print("2. Issuing organization")
        print("3. Date")

        field_choice = input("Enter your choice: ")

        certification = certifications[certification_index]
        certification_id = certification["id"]

        if field_choice == "1":
            certification["name"] = input(
                "Enter the new certification name: "
            )

        elif field_choice == "2":
            certification["organization"] = input(
                "Enter the new issuing organization: "
            )

        elif field_choice == "3":
            certification["date"] = input(
                "Enter the new date: "
            )

        else:
            print("Invalid choice.")
            continue

        update_certification(
            certification_id,
            certification["name"],
            certification["organization"],
            certification["date"]
        )
        print("Certification updated successfully.")

        another = input(
            "Do you want to edit another certification? (yes/no): "
        )

        if another.lower() != "yes":
            break

def edit_projects(saved_resume, resume_id):
    projects = saved_resume["projects"]

    if not projects:
        print("No projects found.")
        return

    while True:
        print("\nPROJECTS")

        for index, project in enumerate(projects, start=1):
            print(
                index,
                project["project_name"]
            )

        project_choice = input(
            "Enter the number of the project you want to edit: "
        )

        if not project_choice.isdigit():
            print("Invalid choice.")
            continue

        project_index = int(project_choice) - 1

        if project_index < 0 or project_index >= len(projects):
            print("Invalid choice.")
            continue

        print("\nWhat would you like to edit?")
        print("1. Project name")
        print("2. Description")
        print("3. Role")
        print("4. Tools/Technologies")
        print("5. Project link")

        field_choice = input("Enter your choice: ")

        project = projects[project_index]
        project_id = project["id"]

        if field_choice == "1":
            project["project_name"] = input(
                "Enter the new project name: "
            )

        elif field_choice == "2":
            project["description"] = input(
                "Enter the new project description: "
            )

        elif field_choice == "3":
            project["role"] = input(
                "Enter your new role: "
            )

        elif field_choice == "4":
            project["tools"] = input(
                "Enter the new tools or technologies: "
            )

        elif field_choice == "5":
            project["project_link"] = input(
                "Enter the new project link: "
            )

        else:
            print("Invalid choice.")
            continue
        update_project(
            project_id,
            project["project_name"],
            project["description"],
            project["role"],
            project["tools"],
            project["project_link"]
        )

        print("Project updated successfully.")

        another = input(
            "Do you want to edit another project? (yes/no): "
        )

        if another.lower() != "yes":
            break

def edit_languages(saved_resume, resume_id):
    languages = saved_resume["languages"]

    if not languages:
        print("No languages found.")
        return

    while True:
        print("\nLANGUAGES")

        for index, language in enumerate(languages, start=1):
            print(
                index,
                language["language"],
                "-",
                language["proficiency"]
            )

        language_choice = input(
            "Enter the number of the language you want to edit: "
        )

        if not language_choice.isdigit():
            print("Invalid choice.")
            continue

        language_index = int(language_choice) - 1

        if language_index < 0 or language_index >= len(languages):
            print("Invalid choice.")
            continue

        print("\nWhat would you like to edit?")
        print("1. Language")
        print("2. Proficiency")

        field_choice = input("Enter your choice: ")

        language = languages[language_index]
        language_id = language["id"]

        if field_choice == "1":
            language["language"] = input(
                "Enter the new language: "
            )

        elif field_choice == "2":
            language["proficiency"] = input(
                "Enter the new proficiency level: "
            )

        else:
            print("Invalid choice.")
            continue

        update_language(
            language_id,
            language["language"],
            language["proficiency"]
    )

        print("Language updated successfully.")

        another = input(
            "Do you want to edit another language? (yes/no): "
        )

        if another.lower() != "yes":
            break

def edit_achievements(saved_resume, resume_id):
    achievements = saved_resume["achievements"]

    if not achievements:
        print("No achievements found.")
        return

    while True:
        print("\nACHIEVEMENTS")

        for index, achievement in enumerate(achievements, start=1):
            print(
                index,
                achievement["title"]
            )

        achievement_choice = input(
            "Enter the number of the achievement you want to edit: "
        )

        if not achievement_choice.isdigit():
            print("Invalid choice.")
            continue

        achievement_index = int(achievement_choice) - 1

        if achievement_index < 0 or achievement_index >= len(achievements):
            print("Invalid choice.")
            continue

        print("\nWhat would you like to edit?")
        print("1. Achievement title")
        print("2. Description")

        field_choice = input("Enter your choice: ")

        achievement = achievements[achievement_index]
        achievement_id = achievement["id"]

        if field_choice == "1":
            achievement["title"] = input(
                "Enter the new achievement title: "
            )

        elif field_choice == "2":
            achievement["description"] = input(
                "Enter the new achievement description: "
            )

        else:
            print("Invalid choice.")
            continue
        update_achievement(
            achievement_id,
            achievement["title"],
            achievement["description"]
    )
        print("Achievement updated successfully.")

        another = input(
            "Do you want to edit another achievement? (yes/no): "
        )

        if another.lower() != "yes":
            break

def edit_volunteer(saved_resume, resume_id):
    volunteer_experiences = saved_resume["volunteer_experience"]

    if not volunteer_experiences:
        print("No volunteer experience found.")
        return

    while True:
        print("\nVOLUNTEER EXPERIENCE")

        for index, volunteer in enumerate(
            volunteer_experiences,
            start=1
        ):
            print(
                index,
                volunteer["role"],
                "-",
                volunteer["organization"]
            )

        volunteer_choice = input(
            "Enter the number of the volunteer experience you want to edit: "
        )

        if not volunteer_choice.isdigit():
            print("Invalid choice.")
            continue

        volunteer_index = int(volunteer_choice) - 1

        if (
            volunteer_index < 0
            or volunteer_index >= len(volunteer_experiences)
        ):
            print("Invalid choice.")
            continue

        print("\nWhat would you like to edit?")
        print("1. Organization")
        print("2. Role")
        print("3. Location")
        print("4. Start date")
        print("5. End date")
        print("6. Description")

        field_choice = input("Enter your choice: ")

        volunteer = volunteer_experiences[volunteer_index]
        volunteer_id = volunteer["id"]

        if field_choice == "1":
            volunteer["organization"] = input(
                "Enter the new organization name: "
            )

        elif field_choice == "2":
            volunteer["role"] = input(
                "Enter the new role: "
            )

        elif field_choice == "3":
            volunteer["location"] = input(
                "Enter the new location: "
            )

        elif field_choice == "4":
            volunteer["start_date"] = input(
                "Enter the new start date: "
            )

        elif field_choice == "5":
            volunteer["end_date"] = input(
                "Enter the new end date: "
            )

        elif field_choice == "6":
            volunteer["description"] = input(
                "Enter the new description: "
            )

        else:
            print("Invalid choice.")
            continue
        
        update_volunteer_experience(
            volunteer_id,
            volunteer["organization"],
            volunteer["role"],
            volunteer["location"],
            volunteer["start_date"],
            volunteer["end_date"],
            volunteer["description"]
        )

        print("Volunteer experience updated successfully.")

        another = input(
            "Do you want to edit another volunteer experience? (yes/no): "
        )

        if another.lower() != "yes":
            break

def edit_references(saved_resume, resume_id):
    references = saved_resume["references"]

    if not references:
        print("No references found.")
        return

    while True:
        print("\nREFERENCES")

        for index, reference in enumerate(references, start=1):
            print(
                index,
                reference["name"],
                "-",
                reference["organization"]
            )

        reference_choice = input(
            "Enter the number of the reference you want to edit: "
        )

        if not reference_choice.isdigit():
            print("Invalid choice.")
            continue

        reference_index = int(reference_choice) - 1

        if reference_index < 0 or reference_index >= len(references):
            print("Invalid choice.")
            continue

        print("\nWhat would you like to edit?")
        print("1. Name")
        print("2. Relationship")
        print("3. Organization")
        print("4. Email")
        print("5. Phone Number")

        field_choice = input("Enter your choice: ")

        reference = references[reference_index]
        reference_id = reference["id"]

        if field_choice == "1":
            reference["name"] = input(
                "Enter the new reference name: "
            )

        elif field_choice == "2":
            reference["relationship"] = input(
                "Enter the new relationship or job title: "
            )

        elif field_choice == "3":
            reference["organization"] = input(
                "Enter the new organization name: "
            )

        elif field_choice == "4":
            reference["email"] = input(
                "Enter the new email: "
            )

        elif field_choice == "5":
            reference["phone_number"] = input(
                "Enter the new phone number: "
            )

        else:
            print("Invalid choice.")
            continue

        update_reference(
            reference_id,
            reference["name"],
            reference["relationship"],
            reference["organization"],
            reference["email"],
            reference["phone_number"]
   )

        print("Reference updated successfully.")

        another = input(
            "Do you want to edit another reference? (yes/no): "
        )

        if another.lower() != "yes":
            break
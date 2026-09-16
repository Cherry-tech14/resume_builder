def edit_resume(saved_resume):
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
        edit_personal_information(saved_resume)

    elif edit_choice == "2":
        edit_summary(saved_resume)

    elif edit_choice == "3":
        edit_education(saved_resume)

    elif edit_choice == "4":
        edit_work_experience(saved_resume)
    
    elif edit_choice == "5":
        edit_skills(saved_resume)

    else:
        print("That editing option has not been implemented yet.")


def edit_personal_information(saved_resume):
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

    print("Personal information updated successfully.")


def edit_summary(saved_resume):
    new_summary = input(
        "Enter your new professional summary: "
    )

    saved_resume["summary"] = new_summary

    print("Professional summary updated successfully.")

def edit_education(saved_resume):
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

    if field_choice == "1":
        education["school"] = input("Enter the new school name: ")

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

    print("Education updated successfully.")

def edit_work_experience(saved_resume):
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

    print("Work experience updated successfully.")
def edit_skills(saved_resume):
    skills = saved_resume["skills"]

    if not skills:
        print("No skills found.")
        return

    while True:
        print("\nSKILLS")

        for index, skill in enumerate(skills, start=1):
            print(index, skill)

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

        skills[skill_index] = new_skill

        print("Skill updated successfully.")

        another = input(
            "Do you want to edit another skill? (yes/no): "
        )

        if another.lower() != "yes":
            break
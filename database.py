import sqlite3

connection = sqlite3.connect(
    "resume.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY,
        name TEXT,
        date_of_birth TEXT,
        email TEXT,
        phone_number TEXT,
        location TEXT,
        summary TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS education (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        school TEXT,
        degree TEXT,
        field TEXT,
        start_year TEXT,
        end_year TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS work_experience (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        job_title TEXT,
        company TEXT,
        location TEXT,
        start_date TEXT,
        end_date TEXT,
        description TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        skill TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS certifications (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        name TEXT,
        organization TEXT,
        date TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        project_name TEXT,
        description TEXT,
        role TEXT,
        tools TEXT,
        project_link TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS languages (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        language TEXT,
        proficiency TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        title TEXT,
        description TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS volunteer_experience (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        organization TEXT,
        role TEXT,
        location TEXT,
        start_date TEXT,
        end_date TEXT,
        description TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_references (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        name TEXT,
        relationship TEXT,
        organization TEXT,
        email TEXT,
        phone_number TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")

connection.commit()


def save_resume(
    name,
    date_of_birth,
    email,
    phone_number,
    location,
    summary
):
    cursor.execute(
        """
        INSERT INTO resumes (
            name,
            date_of_birth,
            email,
            phone_number,
            location,
            summary
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            date_of_birth,
            email,
            phone_number,
            location,
            summary
        )
    )

    connection.commit()

    return cursor.lastrowid

def save_education(
    resume_id,
    school,
    degree,
    field,
    start_year,
    end_year
):
    cursor.execute(
        """
        INSERT INTO education (
            resume_id,
            school,
            degree,
            field,
            start_year,
            end_year
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            resume_id,
            school,
            degree,
            field,
            start_year,
            end_year
        )
    )

    connection.commit()

def save_work_experience(
    resume_id,
    job_title,
    company,
    location,
    start_date,
    end_date,
    description
):
    cursor.execute(
        """
        INSERT INTO work_experience (
            resume_id,
            job_title,
            company,
            location,
            start_date,
            end_date,
            description
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            resume_id,
            job_title,
            company,
            location,
            start_date,
            end_date,
            description
        )
    )

    connection.commit()

def save_skill(resume_id, skill):
    cursor.execute(
        """
        INSERT INTO skills (resume_id, skill)
        VALUES (?, ?)
        """,
        (resume_id, skill)
    )

    connection.commit()

def save_certification(
    resume_id,
    name,
    organization,
    date
):
    cursor.execute(
        """
        INSERT INTO certifications (
            resume_id,
            name,
            organization,
            date
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            resume_id,
            name,
            organization,
            date
        )
    )

    connection.commit()

def save_project(
    resume_id,
    project_name,
    description,
    role,
    tools,
    project_link
):
    cursor.execute(
        """
        INSERT INTO projects (
            resume_id,
            project_name,
            description,
            role,
            tools,
            project_link
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            resume_id,
            project_name,
            description,
            role,
            tools,
            project_link
        )
    )

    connection.commit()

def save_language(
    resume_id,
    language,
    proficiency
):
    cursor.execute(
        """
        INSERT INTO languages (
            resume_id,
            language,
            proficiency
        )
        VALUES (?, ?, ?)
        """,
        (
            resume_id,
            language,
            proficiency
        )
    )

    connection.commit()

def save_achievement(
    resume_id,
    title,
    description
):
    cursor.execute(
        """
        INSERT INTO achievements (
            resume_id,
            title,
            description
        )
        VALUES (?, ?, ?)
        """,
        (
            resume_id,
            title,
            description
        )
    )

    connection.commit()

def save_volunteer_experience(
    resume_id,
    organization,
    role,
    location,
    start_date,
    end_date,
    description
):
    cursor.execute(
        """
        INSERT INTO volunteer_experience (
            resume_id,
            organization,
            role,
            location,
            start_date,
            end_date,
            description
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            resume_id,
            organization,
            role,
            location,
            start_date,
            end_date,
            description
        )
    )

    connection.commit()

def save_reference(
    resume_id,
    name,
    relationship,
    organization,
    email,
    phone_number
):
    cursor.execute(
        """
        INSERT INTO resume_references (
            resume_id,
            name,
            relationship,
            organization,
            email,
            phone_number
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            resume_id,
            name,
            relationship,
            organization,
            email,
            phone_number
        )
    )

    connection.commit()

def load_resume_from_database(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            name,
            date_of_birth,
            email,
            phone_number,
            location,
            summary
        FROM resumes
        WHERE id = ?
        """,
        (resume_id,)
    )
    return cursor.fetchone()

def load_education(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            school,
            degree,
            field,
            start_year,
            end_year
        FROM education
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    education_records = cursor.fetchall()

    education = []

    for record in education_records:
        education.append({
            "id": record[0],
            "school": record[1],
            "degree": record[2],
            "field": record[3],
            "start_year": record[4],
            "end_year": record[5]
        })

    return education

def load_work_experience(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            job_title,
            company,
            location,
            start_date,
            end_date,
            description
        FROM work_experience
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    work_records = cursor.fetchall()
    work_experience = []

    for record in work_records:
        work_experience.append({
            "id": record[0],
            "job_title": record[1],
            "company": record[2],
            "location": record[3],
            "start_date": record[4],
            "end_date": record[5],
            "description": record[6]
        })

    return work_experience

def load_skills(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            skill
        FROM skills
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    skill_records = cursor.fetchall()

    skills = []

    for record in skill_records:
        skills.append({
            "id": record[0],
            "skill": record[1]
        })

    return skills

def load_certifications(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            name,
            organization,
            date
        FROM certifications
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    certification_records = cursor.fetchall()
    certifications = []
    for record in certification_records:
        certifications.append({
            "id": record[0],
            "name": record[1],
            "organization": record[2],
            "date": record[3]
        })
    return certifications

def load_projects(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            project_name,
            description,
            role,
            tools,
            project_link
        FROM projects
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    project_records = cursor.fetchall()
    projects = []
    for record in project_records:
        projects.append({
            "id": record[0],
            "project_name": record[1],
            "description": record[2],
            "role": record[3],
            "tools": record[4],
            "project_link": record[5]
        })
    return projects

def load_languages(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            language,
            proficiency
        FROM languages
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    language_records = cursor.fetchall()
    languages = []
    for record in language_records:
        languages.append({
            "id": record[0],
            "language": record[1],
            "proficiency": record[2]
        })
    return languages

def load_achievements(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            title,
            description
        FROM achievements
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    achievement_records = cursor.fetchall()
    achievements = []
    for record in achievement_records:
        achievements.append({
            "id": record[0],
            "title": record[1],
            "description": record[2]
        })
    return achievements

def load_volunteer_experience(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            organization,
            role,
            location,
            start_date,
            end_date,
            description
        FROM volunteer_experience
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    volunteer_records = cursor.fetchall()
    volunteer_experience = []
    for record in volunteer_records:
        volunteer_experience.append({
            "id": record[0],
            "organization": record[1],
            "role": record[2],
            "location": record[3],
            "start_date": record[4],
            "end_date": record[5],
            "description": record[6]
        })
    return volunteer_experience
        

def load_references(resume_id):
    cursor.execute(
        """
        SELECT
            id,
            name,
            relationship,
            organization,
            email,
            phone_number
        FROM resume_references
        WHERE resume_id = ?
        """,
        (resume_id,)
    )

    reference_records = cursor.fetchall()
    references = []
    for record in reference_records:
        references.append({
            "id": record[0],
            "name": record[1],
            "relationship": record[2],
            "organization": record[3],
            "email": record[4],
            "phone_number": record[5]
        })
    return references

def get_complete_resume(resume_id):
    resume = load_resume_from_database(resume_id)

    if resume is None:
        return None

    return {
        "personal_information": {
            "name": resume[1],
            "date_of_birth": resume[2],
            "email": resume[3],
            "phone_number": resume[4],
            "location": resume[5]
        },
        "summary": resume[6],
        "education": load_education(resume_id),
        "work_experience": load_work_experience(resume_id),
        "skills": load_skills(resume_id),
        "certifications": load_certifications(resume_id),
        "projects": load_projects(resume_id),
        "languages": load_languages(resume_id),
        "achievements": load_achievements(resume_id),
        "volunteer_experience": load_volunteer_experience(resume_id),
        "references": load_references(resume_id)
    }


def update_personal_information(
    resume_id,
    name,
    date_of_birth,
    email,
    phone_number,
    location
):
    cursor.execute(
        """
        UPDATE resumes
        SET
            name = ?,
            date_of_birth = ?,
            email = ?,
            phone_number = ?,
            location = ?
        WHERE id = ?
        """,
        (
            name,
            date_of_birth,
            email,
            phone_number,
            location,
            resume_id
        )
    )

    connection.commit()


def update_summary(resume_id, summary):
    cursor.execute(
        """
        UPDATE resumes
        SET summary = ?
        WHERE id = ?
        """,
        (
            summary,
            resume_id
        )
    )

    connection.commit()

def update_education(
    education_id,
    school,
    degree,
    field,
    start_year,
    end_year
):
    cursor.execute(
        """
        UPDATE education
        SET
            school = ?,
            degree = ?,
            field = ?,
            start_year = ?,
            end_year = ?
        WHERE id = ?
        """,
        (
            school,
            degree,
            field,
            start_year,
            end_year,
            education_id
        )
    )

    connection.commit()

def update_work_experience(
    work_id,
    job_title,
    company,
    location,
    start_date,
    end_date,
    description
):
    cursor.execute(
        """
        UPDATE work_experience
        SET
            job_title = ?,
            company = ?,
            location = ?,
            start_date = ?,
            end_date = ?,
            description = ?
        WHERE id = ?
        """,
        (
            job_title,
            company,
            location,
            start_date,
            end_date,
            description,
            work_id
        )
    )

    connection.commit()

def update_skill(skill_id, skill):
    cursor.execute(
        """
        UPDATE skills
        SET
            skill = ?
        WHERE id = ?
        """,
        (
            skill,
            skill_id
        )
    )

    connection.commit()

def update_certification(
    certification_id,
    name,
    organization,
    date
):
    cursor.execute(
        """
        UPDATE certifications
        SET
            name = ?,
            organization = ?,
            date = ?
        WHERE id = ?
        """,
        (
            name,
            organization,
            date,
            certification_id
        )
    )

    connection.commit()

def update_project(
    project_id,
    project_name,
    description,
    role,
    tools,
    project_link
):
    cursor.execute(
        """
        UPDATE projects
        SET
            project_name = ?,
            description = ?,
            role = ?,
            tools = ?,
            project_link = ?
        WHERE id = ?
        """,
        (
            project_name,
            description,
            role,
            tools,
            project_link,
            project_id
        )
    )

    connection.commit()

def update_language(
    language_id,
    language,
    proficiency
):
    cursor.execute(
        """
        UPDATE languages
        SET
            language = ?,
            proficiency = ?
        WHERE id = ?
        """,
        (
            language,
            proficiency,
            language_id
        )
    )

    connection.commit()

def update_achievement(
    achievement_id,
    title,
    description
):
    cursor.execute(
        """
        UPDATE achievements
        SET
            title = ?,
            description = ?
        WHERE id = ?
        """,
        (
            title,
            description,
            achievement_id
        )
    )

    connection.commit()

def update_volunteer_experience(
    volunteer_id,
    organization,
    role,
    location,
    start_date,
    end_date,
    description
):
    cursor.execute(
        """
        UPDATE volunteer_experience
        SET
            organization = ?,
            role = ?,
            location = ?,
            start_date = ?,
            end_date = ?,
            description = ?
        WHERE id = ?
        """,
        (
            organization,
            role,
            location,
            start_date,
            end_date,
            description,
            volunteer_id
        )
    )

    connection.commit()

def update_reference(
    reference_id,
    name,
    relationship,
    organization,
    email,
    phone_number
):
    cursor.execute(
        """
        UPDATE resume_references
        SET
            name = ?,
            relationship = ?,
            organization = ?,
            email = ?,
            phone_number = ?
        WHERE id = ?
        """,
        (
            name,
            relationship,
            organization,
            email,
            phone_number,
            reference_id
        )
    )

    connection.commit()

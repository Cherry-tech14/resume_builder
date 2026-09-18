import sqlite3


# Connect to the SQLite database
connection = sqlite3.connect("resume.db")

cursor = connection.cursor()


# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
""")


# Create resumes table
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


# Create education table
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


# Create work experience table
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


# Create skills table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        skill TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")


# Create certifications table
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


# Create projects table
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


# Create languages table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS languages (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        language TEXT,
        proficiency TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")


# Create achievements table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS achievements (
        id INTEGER PRIMARY KEY,
        resume_id INTEGER,
        title TEXT,
        description TEXT,
        FOREIGN KEY (resume_id) REFERENCES resumes(id)
    )
""")


# Create volunteer experience table
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


# Create references table
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


# Save changes made while creating tables
connection.commit()


# --------------------------------------------------
# SAVE RESUME
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE EDUCATION
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE WORK EXPERIENCE
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE SKILL
# --------------------------------------------------

def save_skill(resume_id, skill):
    cursor.execute(
        """
        INSERT INTO skills (
            resume_id,
            skill
        )
        VALUES (?, ?)
        """,
        (
            resume_id,
            skill
        )
    )

    connection.commit()


# --------------------------------------------------
# SAVE CERTIFICATION
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE PROJECT
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE LANGUAGE
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE ACHIEVEMENT
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE VOLUNTEER EXPERIENCE
# --------------------------------------------------

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


# --------------------------------------------------
# SAVE REFERENCE
# --------------------------------------------------

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
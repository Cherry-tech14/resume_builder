import sqlite3

connection = sqlite3.connect("resume.db")

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

connection.commit()


def save_resume(name, date_of_birth, email, phone_number, location, summary):
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
resume_id = save_resume(
    "Alex Johnson",
    "1998-05-10",
    "alex@example.com",
    "08012345678",
    "Abuja",
    "Motivated professional with experience in administration."
)

print("Resume saved with ID:", resume_id)

def save_education(resume_id, school, degree, field, start_year, end_year):
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

save_education(
    resume_id,
    "University of Abuja",
    "BSc",
    "Banking and Finance",
    "2018",
    "2022"
)

print("Education saved.")


cursor.execute("""
    SELECT * FROM education
    WHERE resume_id = ?
""", (resume_id,))

education_records = cursor.fetchall()

print("Education records:", education_records)
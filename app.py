from flask import Flask, render_template, request, redirect, session, flash, jsonify, url_for
from weasyprint import HTML
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_all_resumes
from database import delete_resume
import re
from datetime import datetime
import os
from dotenv import load_dotenv
from google import genai
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from email.message import EmailMessage
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf.csrf import CSRFProtect
import hashlib
import secrets
import smtplib


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)
else:
    client = None

from database import (
    get_complete_resume,
    save_resume,
    save_user,
    get_user_by_username,
    get_user_by_email,
    get_user_password_hash,
    save_education,
    save_work_experience,
    save_skill,
    save_certification,
    save_project,
    save_language,
    save_achievement,
    save_volunteer_experience,
    save_reference,
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
    update_reference,
    update_user_password
)


app = Flask(__name__)
app.secret_key = os.environ["FLASK_SECRET_KEY"]
csrf = CSRFProtect(app)
reset_serializer = URLSafeTimedSerializer(
    app.secret_key,
    salt="password-reset"
)

limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://"
)

@app.errorhandler(429)
def ratelimit_handler(error):
    return render_template(
        "forgot_password.html",
        error="Too many password reset requests. Please try again in 15 minutes."
    ), 429

def generate_reset_token(user_id):
    password_hash = get_user_password_hash(user_id)

    if password_hash is None:
        return None

    password_fingerprint = hashlib.sha256(
        password_hash.encode("utf-8")
    ).hexdigest()

    token = reset_serializer.dumps({
        "user_id": user_id,
        "password_fingerprint": password_fingerprint
    })

    return token


def verify_reset_token(token):
    try:
        data = reset_serializer.loads(
            token,
            max_age=1800
        )

        user_id = data["user_id"]
        token_fingerprint = data["password_fingerprint"]

        current_password_hash = get_user_password_hash(user_id)

        if current_password_hash is None:
            return None

        current_fingerprint = hashlib.sha256(
            current_password_hash.encode("utf-8")
        ).hexdigest()

        if not secrets.compare_digest(
            token_fingerprint,
            current_fingerprint
        ):
            return None

        return user_id

    except (BadSignature, SignatureExpired, KeyError, TypeError, ValueError):
        return None

def send_reset_email(recipient_email, reset_link):

    sender_email = os.getenv("MAIL_USERNAME")
    app_password = os.getenv("MAIL_PASSWORD")

    if not sender_email or not app_password:
        raise RuntimeError("Email settings are missing.")

    message = EmailMessage()

    message["Subject"] = "Reset Your Resume Builder Password"
    message["From"] = sender_email
    message["To"] = recipient_email

    message.set_content(
        f"""Hello,

We received a request to reset your Resume Builder password.

Click the link below to create a new password:

{reset_link}

This link will expire after 30 minutes.

If you did not request a password reset, you can ignore this email.

"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
        server.login(sender_email, app_password)
        server.send_message(message)

def validate_resume(form):
    errors = []

    name = form.get("name", "").strip()
    email = form.get("email", "").strip()
    phone = form.get("phone_number", "").strip()
    summary = form.get("summary", "").strip()

    if not name:
        errors.append("Full name is required.")

    if not email:
        errors.append("Email is required.")
    elif not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        errors.append("Enter a valid email address.")

    if not phone:
        errors.append("Phone number is required.")

    if not summary:
        errors.append("Professional summary is required.")

    for section, start_field, end_field in [
        ("Education", "start_year", "end_year"),
        ("Work Experience", "start_date", "end_date"),
        ("Volunteer Experience", "volunteer_start_date", "volunteer_end_date")
    ]:
        starts = form.getlist(start_field)
        ends = form.getlist(end_field)

        for start, end in zip(starts, ends):
            error = validate_dates(start, end, section)

            if error:
                errors.append(error)


    for key in form.keys():
        for section, start_prefix, end_prefix in [
            ("Education", "start_year_", "end_year_"),
            ("Work Experience", "start_date_", "end_date_"),
            ("Volunteer Experience", "volunteer_start_date_", "volunteer_end_date_")
        ]:
            if key.startswith(start_prefix):
                record_id = key[len(start_prefix):]

                error = validate_dates(
                    form.get(key),
                    form.get(f"{end_prefix}{record_id}"),
                    section
                )

                if error:
                    errors.append(error)

    return errors

def validate_dates(start, end, section):
    start = (start or "").strip()
    end = (end or "").strip()

    if not start or not end:
        return None

    if end.lower() in ("present", "current"):
        return None

    def parse_date(value):
        for date_format in ("%Y-%m-%d", "%Y-%m", "%Y"):
            try:
                return datetime.strptime(value, date_format)
            except ValueError:
                continue

        return None

    start_date = parse_date(start)
    end_date = parse_date(end)

    if start_date is None or end_date is None:
        return (
            f"{section}: Use YYYY, YYYY-MM, or YYYY-MM-DD "
            "for dates."
        )

    if end_date < start_date:
        return f"{section}: End date cannot be before start date."

    return None


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-summary", methods=["POST"])
def generate_summary():

    if "user_id" not in session:
        return jsonify({"error": "Please log in first."}), 401

    if client is None:
        return jsonify({"error": "Gemini API key is not configured."}), 503

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid request data."}), 400

    job_title = data.get("job_title", "")
    skills = data.get("skills", [])

    if not isinstance(job_title, str) or not isinstance(skills, list):
        return jsonify({"error": "Invalid job title or skills."}), 400

    if not all(isinstance(skill, str) for skill in skills):
        return jsonify({"error": "Skills must be text."}), 400

    job_title = job_title.strip()[:150]
    skills = [skill.strip()[:100] for skill in skills[:30] if skill.strip()]

    if not job_title and not skills:
        return jsonify({
            "error": "Please enter a job title or at least one skill."
        }), 400

    prompt = f"""
    Write a professional resume summary using the information below.

    Job title: {job_title or "Not provided"}
    Skills: {", ".join(skills) if skills else "Not provided"}

    Requirements:
    - Write 2 to 3 sentences.
    - Use professional, clear language.
    - Highlight the skills provided.
    - Do not invent qualifications, achievements, or work experience.
    - Do not claim years of experience unless explicitly provided.
    - Do not include a heading.
    - Return only the professional summary.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        summary = (response.text or "").strip()

        if not summary:
            return jsonify({
                "error": "Gemini returned an empty summary. Please try again."
            }), 502

        return jsonify({"summary": summary})

    except Exception:
        app.logger.exception("Gemini summary generation failed")

        return jsonify({
            "error": "Unable to generate a summary right now. Please try again."
        }), 503


@app.route("/improve-summary", methods=["POST"])
def improve_summary():

    if "user_id" not in session:
        return jsonify({"error": "Please log in first."}), 401

    if client is None:
        return jsonify({"error": "Gemini API key is not configured."}), 503

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid request data."}), 400

    summary = data.get("summary", "")

    if not isinstance(summary, str):
        return jsonify({"error": "Summary must be text."}), 400

    summary = summary.strip()

    if not summary:
        return jsonify({"error": "Please enter a summary first."}), 400

    if len(summary) > 5000:
        return jsonify({"error": "Summary is too long."}), 400

    prompt = f"""
    Improve the following professional resume summary:

    {summary}

    Requirements:
    - Use clear and professional language.
    - Keep it concise, preferably 2 to 3 sentences.
    - Correct grammar and improve readability.
    - Preserve the original meaning.
    - Do not invent qualifications, skills, or achievements.
    - Do not include a heading.
    - Return only the improved summary.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        improved_summary = (response.text or "").strip()

        if not improved_summary:
            return jsonify({
                "error": "Gemini returned an empty summary."
            }), 502

        return jsonify({"summary": improved_summary})

    except Exception:
        app.logger.exception("Gemini summary improvement failed")

        return jsonify({
            "error": "Unable to improve summary right now."
        }), 503

@app.route("/generate-description", methods=["POST"])
def generate_description():

    if "user_id" not in session:
        return jsonify({"error": "Please log in first."}), 401

    data = request.get_json(silent=True) or {}

    job_title = data.get("job_title", "").strip()
    description = data.get("description", "").strip()
    section = data.get("section", "work_experience")

    if section not in ("work_experience", "project"):
        return jsonify({
            "error": "Invalid resume section"
        }), 400

    if not job_title or not description:
        return jsonify({
            "error": "A title and description are required."
        }), 400

    if client is None:
        return jsonify({
            "error": "Gemini AI is not configured."
        }), 503

    section_name = (
        "software project"
        if section == "project"
        else "work experience"
    ) 

    prompt = f"""
    You are a professional resume writing assistant.

    Improve the following work experience description.

    Job Title: {job_title}

    Original Description: {description}

    Requirements:
    - Use professional resume language.
    - Use clear and concise sentences.
    - Start statements with strong action verbs.
    - Do not invent responsibilities, achievements, or statistics.
    - Preserve the user's actual experience.
    - Return only the improved description.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        improved_description = (response.text or "").strip()

        if not improved_description:
            return jsonify({
                "error": "AI returned an empty description."
            }), 502

        return jsonify({
            "description": improved_description
        })

    except Exception:
        app.logger.exception("Gemini description generation failed")
        return jsonify({
            "error": "Unable to improve the description right now. Please try again."
        }), 500

@app.route("/create", methods=["GET", "POST"])
def create_resume():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        errors = validate_resume(request.form)
        if errors:
            return render_template(
                "create_resume.html",
                errors=errors
            ), 400

        name = request.form["name"].strip()
        email = request.form["email"]
        date_of_birth = request.form["date_of_birth"]
        phone_number = request.form["phone_number"]
        location = request.form["location"]

        summary = request.form["summary"]

        template = request.form["template"]

        schools = request.form.getlist("school")
        degrees = request.form.getlist("degree")
        fields = request.form.getlist("field")
        start_years = request.form.getlist("start_year")
        end_years = request.form.getlist("end_year")

        
        job_titles = request.form.getlist("job_title")
        companies = request.form.getlist("company")
        work_locations = request.form.getlist("work_location")
        start_dates = request.form.getlist("start_date")
        end_dates = request.form.getlist("end_date")
        descriptions = request.form.getlist("description")

        skills = request.form.getlist("skill")
       

        certification_names = request.form.getlist("certification_name")
        certification_organizations = request.form.getlist("certification_organization")
        certification_dates = request.form.getlist("certification_date")

        
        project_names = request.form.getlist("project_name")
        project_descriptions = request.form.getlist("project_description")
        project_roles = request.form.getlist("project_role")
        project_tools_list = request.form.getlist("project_tools")
        project_links = request.form.getlist("project_link")

        
        languages = request.form.getlist("language")
        language_proficiencies = request.form.getlist("language_proficiency")

    
        achievement_titles = request.form.getlist("achievement_title")
        achievement_descriptions = request.form.getlist(
            "achievement_description"
        )

        
        volunteer_organizations = request.form.getlist("volunteer_organization")
        volunteer_roles = request.form.getlist("volunteer_role")
        volunteer_locations = request.form.getlist("volunteer_location")
        volunteer_start_dates = request.form.getlist("volunteer_start_date")
        volunteer_end_dates = request.form.getlist("volunteer_end_date")
        volunteer_descriptions = request.form.getlist("volunteer_description")

    
        reference_names = request.form.getlist("reference_name")
        reference_relationships = request.form.getlist("reference_relationship")
        reference_organizations = request.form.getlist("reference_organization")
        reference_emails = request.form.getlist("reference_email")
        reference_phone_numbers = request.form.getlist("reference_phone_number")

    
        resume_id = save_resume(
            name,
            date_of_birth,
            email,
            phone_number,
            location,
            summary,
            template,
            session["user_id"]
        )

    
        for school, degree, field, start_year, end_year in zip(
            schools,
            degrees,
            fields,
            start_years,
            end_years
        ):
            if school or degree or field or start_year or end_year:
                save_education(
                    resume_id,
                    school,
                    degree,
                    field,
                    start_year,
                    end_year
                )

        
        for (
            job_title,
            company,
            work_location,
            start_date,
            end_date,
            description
        ) in zip(
            job_titles,
            companies,
            work_locations,
            start_dates,
            end_dates,
            descriptions
        ):
            if (
                job_title
                or company
                or work_location
                or start_date
                or end_date
                or description
        ):
                save_work_experience(
                    resume_id,
                    job_title,
                    company,
                    work_location,
                    start_date,
                    end_date,
                   description
                )  

        
        for skill in skills:
            if skill:
                save_skill(resume_id, skill)

        
        for (
            name,
            organization,
            date,
        ) in zip(
            certification_names,
            certification_organizations,
            certification_dates

        ):
            if name or organization or date:
                save_certification(
                    resume_id,
                    name,
                    organization,
                    date
            )

        
        for (
            project_name,
            project_description,
            project_role,
            project_tools,
            project_link
        ) in zip(
            project_names,
            project_descriptions,
            project_roles,
            project_tools_list,
            project_links
        ):
            if (
                project_name
                or project_description
                or project_role
                or project_tools
                or project_link
            ):
                save_project(
                    resume_id,
                    project_name,
                    project_description,
                    project_role,
                    project_tools,
                    project_link
                )

        
        for language, proficiency in zip(
            languages,
            language_proficiencies
        ):
            if language or proficiency:
                save_language(
                    resume_id,
                    language,
                    proficiency
                )


        for title, description in zip(
            achievement_titles,
            achievement_descriptions
        ):
            if title or description:
                save_achievement(
                    resume_id,
                    title,
                    description
                )

        
        for (
            organization,
            role,
            location,
            start_date,
            end_date,
            description
        ) in zip(
            volunteer_organizations,
            volunteer_roles,
            volunteer_locations,
            volunteer_start_dates,
            volunteer_end_dates,
            volunteer_descriptions
        ):
            if (
                organization
                or role
                or location
                or start_date
                or end_date
                or description

            ):
                save_volunteer_experience(
                    resume_id,
                    organization,
                    role,
                    location,
                    start_date,
                    end_date,
                    description
            )

        for (
            name,
            relationship,
            organization,
            email,
            phone_number
        ) in zip(
            reference_names,
            reference_relationships,
            reference_organizations,
            reference_emails,
            reference_phone_numbers

        ):
            if (
                name
                or relationship
                or organization
                or email
                or phone_number
            ):
                save_reference(
                    resume_id,
                    name,
                    relationship,
                    organization,
                    email,
                    phone_number
            )

        flash("Resume created successfully", "success")
        return redirect("/dashboard")
    return render_template("create_resume.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if not username or not email or not password or not confirm_password:
            return render_template(
                "register.html",
                error="All fields are required."
            )

        if password != confirm_password:
            return render_template(
                "register.html",
                error="Passwords do not match."
            )

        existing_user = get_user_by_username(username)

        if existing_user:
            return render_template(
                "register.html",
                error="Username already exists."
            )

        existing_email = get_user_by_email(email)

        if existing_email:
            return render_template(
                "register.html",
                error="Email address already registered."
            )

        password_hash = generate_password_hash(password)

        save_user(username, email, password_hash)

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = get_user_by_username(username)

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Invalid username or password."
        )

    return render_template("login.html")

@app.route("/forgot-password", methods=["GET", "POST"])
@limiter.limit("3 per 15 minutes", methods=["POST"])
def forgot_password():

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()

        if not email:
            return render_template(
                "forgot_password.html",
                error="Please enter your email address."
            )

        user = get_user_by_email(email)

        if user:
            user_id = user[0]

            token = generate_reset_token(user_id)

            if token is not None:
                reset_link = url_for(
                    "reset_password",
                    token=token,
                    _external=True
                )

                try:
                    send_reset_email(email, reset_link)

                except (smtplib.SMTPException, OSError) as error:
                    app.logger.error(
                        "Password reset email could not be sent: %s",
                        type(error).__name__
                    )

        return render_template(
            "forgot_password.html",
            message=(
                "If an account exists with this email, "
                "password reset instructions will be sent."
            )
        )

    return render_template("forgot_password.html")

@app.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):

    user_id = verify_reset_token(token)

    if user_id is None:
        return render_template(
            "reset_password.html",
            error="This password reset link is invalid or has expired.",
            invalid_token=True
        )

    if request.method == "POST":
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if len(password) < 8:
            return render_template(
                "reset_password.html",
                error="Password must contain at least 8 characters."
            )

        if password != confirm_password:
            return render_template(
                "reset_password.html",
                error="Passwords do not match."
            )

        password_hash = generate_password_hash(password)

        update_user_password(user_id, password_hash)

        flash("Password updated successfully. Please log in.")

        return redirect(url_for("login"))

    return render_template("reset_password.html")

@app.route("/dashboard")
def dashboard():
    resumes = get_all_resumes()

    total_resumes = len(resumes)
    return render_template(
        "dashboard.html",
        resumes=resumes,
        total_resumes=total_resumes
    )

@app.route("/resume/<int:resume_id>/delete", methods=["POST"])
def remove_resume(resume_id):

    deleted = delete_resume(resume_id)

    if not deleted:
        flash("Resume not found", "error")
        return redirect("/dashboard")

    flash("Resume deleted successfully", "success")
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/resume/<int:resume_id>")
def view_resume(resume_id):

    resume = get_complete_resume(resume_id)

    if not resume:
        return "Resume not found", 404

    if resume["template"] == "modern":
        template_file = "resume_modern.html"
    else:
        template_file = "resume.html"

    return render_template(
        template_file,
        resume=resume
    )

@app.route("/resume/<resume_id>/pdf")
def download_pdf(resume_id):
    if "user_id" not in session:
        return redirect("/login")
    resume = get_complete_resume(int(resume_id))

    if resume is None:
        return "Resume not found."

    if resume["template"] == "modern":
        template_file = "resume_modern.html"
    else:
        template_file = "resume.html"

    html = render_template(
        template_file,
        resume=resume,
        pdf=True
    )

    pdf = HTML(
        string=html,
        base_url=request.url_root
    ).write_pdf()

    return pdf, 200, {
        "Content-Type": "application/pdf",
        "Content-Disposition": "attachment; filename=resume.pdf"
    }

@app.route("/resume")
def find_resume():

    resume_id = request.args.get("resume_id")

    return redirect(f"/resume/{resume_id}")


@app.route("/edit/<resume_id>", methods=["GET", "POST"])
def edit_resume(resume_id):
    if "user_id" not in session:
        return redirect("/login")

    resume = get_complete_resume(int(resume_id))

    if resume is None:
        return "Resume not found."

    if request.method == "POST":

        errors = validate_resume(request.form)

        if errors:
            return render_template(
                "edit_resume.html",
                resume=resume,
                errors=errors
            ), 400

        name = request.form["name"].strip()
        date_of_birth = request.form["date_of_birth"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        location = request.form["location"]

        update_personal_information(
            resume_id,
            name,
            date_of_birth,
            email,
            phone_number,
            location
        )


        summary = request.form["summary"]

        update_summary(
            resume_id,
            summary
        )

      
        for education in resume["education"]:

            education_id = education["id"]

            school = request.form.get(
                f"school_{education_id}"
            )

            degree = request.form.get(
                f"degree_{education_id}"
            )

            field = request.form.get(
                f"field_{education_id}"
            )

            start_year = request.form.get(
                f"start_year_{education_id}"
            )

            end_year = request.form.get(
                f"end_year_{education_id}"
            )

            update_education(
                education_id,
                school,
                degree,
                field,
                start_year,
                end_year
            )

       
        for experience in resume["work_experience"]:

            experience_id = experience["id"]

            job_title = request.form.get(
                f"job_title_{experience_id}"
            )

            company = request.form.get(
                f"company_{experience_id}"
            )

            work_location = request.form.get(
                f"work_location_{experience_id}"
            )

            start_date = request.form.get(
                f"start_date_{experience_id}"
            )

            end_date = request.form.get(
                f"end_date_{experience_id}"
            )

            description = request.form.get(
                f"description_{experience_id}"
            )

            update_work_experience(
                experience_id,
                job_title,
                company,
                work_location,
                start_date,
                end_date,
                description
            )

        for skill in resume["skills"]:

            skill_id = skill["id"]

            skill_value = request.form.get(
                f"skill_{skill_id}"
            )

            update_skill(
                skill_id,
                skill_value
            )


        for certification in resume["certifications"]:

            certification_id = certification["id"]

            name = request.form.get(
                f"certification_name_{certification_id}"
            )

            organization = request.form.get(
                f"certification_organization_{certification_id}"
            )

            date = request.form.get(
                f"certification_date_{certification_id}"
            )

            update_certification(
                certification_id,
                name,
                organization,
                date
            )


        for project in resume["projects"]:

            project_id = project["id"]

            project_name = request.form.get(
                f"project_name_{project_id}"
            )

            project_description = request.form.get(
                f"project_description_{project_id}"
            )

            project_role = request.form.get(
                f"project_role_{project_id}"
            )

            project_tools = request.form.get(
                f"project_tools_{project_id}"
            )

            project_link = request.form.get(
                f"project_link_{project_id}"
            )

            update_project(
                project_id,
                project_name,
                project_description,
                project_role,
                project_tools,
                project_link
            )


        for language in resume["languages"]:

            language_id = language["id"]

            language_value = request.form.get(
                f"language_{language_id}"
            )

            proficiency = request.form.get(
                f"language_proficiency_{language_id}"
            )

            update_language(
                language_id,
                language_value,
                proficiency
            )

        for achievement in resume["achievements"]:

            achievement_id = achievement["id"]

            title = request.form.get(
                f"achievement_title_{achievement_id}"
            )

            description = request.form.get(
                f"achievement_description_{achievement_id}"
            )

            update_achievement(
                achievement_id,
                title,
                description
            )

        for volunteer in resume["volunteer_experience"]:

            volunteer_id = volunteer["id"]

            organization = request.form.get(
                f"volunteer_organization_{volunteer_id}"
            )

            role = request.form.get(
                f"volunteer_role_{volunteer_id}"
            )

            location = request.form.get(
                f"volunteer_location_{volunteer_id}"
            )

            start_date = request.form.get(
                f"volunteer_start_date_{volunteer_id}"
            )

            end_date = request.form.get(
                f"volunteer_end_date_{volunteer_id}"
            )

            description = request.form.get(
                f"volunteer_description_{volunteer_id}"
            )

            update_volunteer_experience(
                volunteer_id,
                organization,
                role,
                location,
                start_date,
                end_date,
                description
            )

        for reference in resume["references"]:

            reference_id = reference["id"]

            name = request.form.get(
                f"reference_name_{reference_id}"
            )

            relationship = request.form.get(
                f"reference_relationship_{reference_id}"
            )

            organization = request.form.get(
                f"reference_organization_{reference_id}"
            )

            email = request.form.get(
                f"reference_email_{reference_id}"
            )

            phone_number = request.form.get(
                f"reference_phone_number_{reference_id}"
            )

            update_reference(
                reference_id,
                name,
                relationship,
                organization,
                email,
                phone_number
            )

        return redirect(f"/resume/{resume_id}")

    return render_template(
        "edit_resume.html",
        resume=resume
    )

if __name__ == "__main__":
    app.run(debug=True)
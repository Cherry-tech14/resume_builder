# AI-Powered Resume Builder

An AI-powered web application that helps users create, edit, manage, and download professional resumes.

Built with **Python, Flask, SQLite, HTML, CSS, JavaScript, and Google Gemini AI**, the application provides a user-friendly interface for building resumes and improving their content with artificial intelligence.

## Features

### User Authentication
- User registration and login.
- Secure password hashing.
- Password reset functionality through email.
- User-specific dashboards.

### Resume Management
- Create professional resumes.
- Save resumes for future editing.
- Update personal information, education, work experience, and other resume sections.
- View saved resumes on a personal dashboard.
- Delete resumes that are no longer needed.

### AI-Powered Writing Assistance
Uses Google Gemini AI to help users improve their:

- Professional summaries.
- Work experience descriptions.
- Project descriptions.
- Volunteer experience descriptions.

### Resume Templates
Users can select from available resume templates to customize their resumes.

### PDF Generation
Users can download their completed resumes as PDF documents using WeasyPrint.

### Security
- Password hashing.
- Session-based authentication.
- CSRF protection.
- Rate limiting.
- Ownership checks for protected resume operations.
- Environment variables for sensitive configuration.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| SQLite | Database |
| HTML | Website structure |
| CSS | Website styling |
| JavaScript | Frontend interactivity |
| Jinja2 | HTML template rendering |
| Google Gemini AI | AI-powered writing assistance |
| WeasyPrint | PDF generation |
| Flask-WTF | CSRF protection |
| Flask-Limiter | Request rate limiting |
| Git and GitHub | Version control |

## Project Structure

The main project files include:

```text
resume_builder/
│
├── app.py
├── database.py
├── requirements.txt
├── templates/
├── static/
├── .gitignore
└── README.md
```

**File descriptions:**

- `app.py`: Handles Flask routes and application functionality.
- `database.py`: Handles database operations.
- `requirements.txt`: Lists Python dependencies.
- `templates/`: Contains HTML templates.
- `static/`: Contains frontend assets.
- `.gitignore`: Excludes sensitive and unnecessary files from version control.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Cherry-tech14/resume_builder.git
```

Navigate into the project:

```bash
cd resume_builder
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

WeasyPrint may require additional operating-system libraries depending on the environment.

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
FLASK_SECRET_KEY=your_flask_secret_key
MAIL_USERNAME=your_email_address
MAIL_PASSWORD=your_email_app_password
```

Replace the example values with your own credentials.

**Security:** Never commit `.env`, API keys, passwords, or other credentials to GitHub.

### 5. Run the Application

```bash
python3 app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How to Use

1. Register an account.
2. Log in to your dashboard.
3. Create a new resume.
4. Enter your personal and professional information.
5. Use AI assistance to improve selected resume sections.
6. Choose a resume template.
7. Save and preview your resume.
8. Download your resume as a PDF.
9. Return later to edit or delete saved resumes.

## Current Project Status

**Version 1 — Local Development Completed**

The core application features have been implemented and tested locally.

The project is not currently deployed publicly.

Additional production preparation, including database connection management, persistent storage, backups, and deployment testing, is required before opening registration to real users.

## Future Improvements

Potential future improvements include:

- Public deployment.
- Additional resume templates.
- Improved mobile responsiveness.
- More AI-powered resume suggestions.
- Automated testing and performance improvements.
- Production-ready database management and backups.

## Author

**Mariam Mohammed**

Aspiring Full-Stack Software Developer

GitHub: Cherry-tech14

## License

No license has been specified for this project.
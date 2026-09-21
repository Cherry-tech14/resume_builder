from flask import Flask, render_template

from database import get_complete_resume

app = Flask(__name__)


@app.route("/")
def home():
    return "Resume Builder is running"


@app.route("/resume/<resume_id>")
def view_resume(resume_id):
    resume = get_complete_resume(int(resume_id))

    if resume is None:
        return "Resume not found."

    return render_template(
        "resume.html",
        resume=resume
    )


if __name__ == "__main__":
    app.run(debug=True)
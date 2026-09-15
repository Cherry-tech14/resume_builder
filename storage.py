import json

def save_resume(resume):
    with open("resume.json", "w") as file:
        json.dump(resume, file, indent=4)

def load_resume():
    try:
        with open("resume.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None
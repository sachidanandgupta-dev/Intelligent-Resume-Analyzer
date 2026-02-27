import re

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_resume(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()

    def extract_email(self, text):
        pattern = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+"
        match = re.search(pattern, text)
        return match.group() if match else None

    def extract_name(self, text):
        return text.split("\n")[0]

    def extract_skills(self, text):
        predefined_skills = ["Python", "SQL", "Machine Learning", "Communication", "Git"]
        found = []
        for skill in predefined_skills:
            if skill.lower() in text.lower():
                found.append(skill)
        return found

    def parse(self):
        text = self.read_resume()

        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "skills": self.extract_skills(text)
        }
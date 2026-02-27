class ResumeMatcher:
    def __init__(self, candidate_data, job_requirements):
        self.candidate_skills = candidate_data["skills"]
        self.required_skills = job_requirements["skills"]

    def calculate_match(self):
        matched = list(set(self.candidate_skills) & set(self.required_skills))
        missing = list(set(self.required_skills) - set(self.candidate_skills))

        score = int((len(matched) / len(self.required_skills)) * 100)

        return score, missing
class ReportGenerator:
    def __init__(self, candidate_data, score, missing_skills):
        self.data = candidate_data
        self.score = score
        self.missing = missing_skills

    def recommendation(self):
        if self.score >= 80:
            return "Strong Match"
        elif self.score >= 60:
            return "Moderate Match"
        else:
            return "Weak Match"

    def generate(self):
        return {
            "Name": self.data["name"],
            "Email": self.data["email"],
            "Skills": self.data["skills"],
            "Match Score": self.score,
            "Missing Skills": self.missing,
            "Recommendation": self.recommendation()
        }
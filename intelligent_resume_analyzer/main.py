from parser import ResumeParser
from matcher import ResumeMatcher
from report_generator import ReportGenerator
import json

def main():
    resume_file = "sample_resume.txt"

    job_requirements = {
        "skills": ["Python", "Machine Learning", "SQL", "Communication", "Git"]
    }

    parser = ResumeParser(resume_file)
    candidate_data = parser.parse()

    matcher = ResumeMatcher(candidate_data, job_requirements)
    score, missing = matcher.calculate_match()

    report = ReportGenerator(candidate_data, score, missing)
    result = report.generate()

    with open("analysis_report.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Analysis Completed!")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()





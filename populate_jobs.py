from database.db import SessionLocal
from database.models import Job

sample_jobs = [
    {
        "title": "Python Developer",
        "company": "Tech Solutions",
        "location": "Bangalore",
        "skills": "python, django, rest, postgresql"
    },
    {
        "title": "Data Analyst",
        "company": "DataCorp",
        "location": "Mumbai",
        "skills": "sql, pandas, excel, python"
    },
    {
        "title": "Machine Learning Engineer",
        "company": "AI Innovators",
        "location": "Hyderabad",
        "skills": "python, scikit-learn, tensorflow, numpy"
    },
    {
        "title": "Frontend Developer",
        "company": "WebStudio",
        "location": "Chennai",
        "skills": "html, css, javascript, react"
    },
    {
        "title": "DevOps Engineer",
        "company": "CloudBase",
        "location": "Pune",
        "skills": "docker, kubernetes, aws, ci/cd"
    }
]

def insert_sample_jobs():
    db = SessionLocal()
    try:
        for job_data in sample_jobs:
            job = Job(**job_data)
            db.add(job)
        db.commit()
        print("✅ Sample job data inserted successfully.")
    finally:
        db.close()

if __name__ == "__main__":
    insert_sample_jobs()

from sqlalchemy.orm import Session
from database.models import Job
from database.db import SessionLocal
import pandas as pd

def load_job_data():
    """
    Load job postings from the database and return as a Pandas DataFrame.
    """
    try:
        db: Session = SessionLocal()
        jobs = db.query(Job).all()
        job_data = [
            {
                "id": job.id,
                "title": job.title,
                "company": job.company,
                "location": job.location,
                "skills": job.skills
            }
            for job in jobs
        ]
        return pd.DataFrame(job_data)
    except Exception as e:
        raise RuntimeError(f"Error loading jobs from DB: {e}")
    finally:
        db.close()

def preprocess_skills(skills: list) -> str:
    """
    Preprocess user input skills (list of strings) into a single lowercase string.
    """
    return " ".join(skills).lower()



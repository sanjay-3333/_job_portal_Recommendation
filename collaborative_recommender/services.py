from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.models import Interaction, Job
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def load_interaction_data():
    db: Session = SessionLocal()
    interactions = db.query(Interaction).all()
    db.close()

    data = []
    for i in interactions:
        user_id = int.from_bytes(i.user_id, "little") if isinstance(i.user_id, bytes) else int(i.user_id)
        job_id = int.from_bytes(i.job_id, "little") if isinstance(i.job_id, bytes) else int(i.job_id)
        interaction = int(i.interaction) if i.interaction is not None else 1

        data.append({
            "user_id": user_id,
            "job_id": job_id,
            "interaction": interaction
        })

    return pd.DataFrame(data)


def create_user_job_matrix(df: pd.DataFrame):
    return df.pivot_table(index="user_id", columns="job_id", values="interaction").fillna(0)


def generate_similarity_matrix(user_job_matrix):
    return cosine_similarity(user_job_matrix)


def load_job_metadata():
    db: Session = SessionLocal()
    jobs = db.query(Job).all()
    db.close()

    return pd.DataFrame([{
        "job_id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "skills": job.skills
    } for job in jobs])

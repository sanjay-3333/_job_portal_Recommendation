from database.db import engine, SessionLocal
from database.models import Base, Job, Interaction
import pandas as pd

# Create tables
Base.metadata.create_all(bind=engine)

# ✅ Load and insert job data
df = pd.read_csv("data/jobs.csv").fillna("")

session = SessionLocal()
for _, row in df.iterrows():
    job = Job(
        title=row["title"],
        company=row["company"],
        location=row["location"],
        skills=row["skills"].lower()
    )
    session.add(job)
session.commit()
print("✅ Jobs loaded into database.")

# ✅ Load and insert interaction data with casting
interaction_df = pd.read_csv("data/interactions.csv")
for _, row in interaction_df.iterrows():
    interaction = Interaction(
        user_id=int(row["user_id"]),
        job_id=int(row["job_id"]),
        interaction=int(row["interaction"])  # ✅ Ensure this column exists in CSV
    )
    session.add(interaction)
session.commit()
session.close()
print("✅ Interactions loaded into database.")

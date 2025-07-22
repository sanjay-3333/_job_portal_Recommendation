from database.db import SessionLocal
from database.models import Interaction

session = SessionLocal()
interactions = session.query(Interaction).all()
print(f"Total interactions: {len(interactions)}")
for inter in interactions:
    print(f"user_id={inter.user_id}, job_id={inter.job_id}, interaction={inter.interaction}")
session.close()

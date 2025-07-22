from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    user_id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), primary_key=True)
    interaction = Column(Integer, default=1)

    job = relationship("Job", back_populates="interactions")

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    skills = Column(String)

    interactions = relationship("Interaction", back_populates="job")

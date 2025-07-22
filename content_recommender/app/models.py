from pydantic import BaseModel
from typing import List

class SkillInput(BaseModel):
    skills: List[str]

class InteractionInput(BaseModel):
    user_id: int
    job_id: int
    interaction: int

class HybridRequest(BaseModel):
    user_id: int
    skills: List[str]
    top_n: int = 5

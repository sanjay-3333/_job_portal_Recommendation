from pydantic import BaseModel
from typing import List

class InteractionInput(BaseModel):
    user_id: int
    job_id: int
    interaction: int
    top_n: int = 5

class HybridRequest(BaseModel):
    user_id: int
    skills: List[str]
    top_n: int = 5
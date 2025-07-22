from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .recommender import recommend_hybrid

router = APIRouter(
    prefix="/recommend/hybrid",
    tags=["Hybrid Recommendation"]
)

# Request model
class HybridRequest(BaseModel):
    user_id: int
    skills: str
    top_n: int = 5

@router.post("/recommend")
def hybrid_route(req: HybridRequest):
    try:
        recommendations = recommend_hybrid(req.user_id, req.skills, req.top_n)
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, HTTPException
from .models import SkillInput
from .services import load_job_data, preprocess_skills
from .recommender import ContentRecommender

router = APIRouter()

job_df = load_job_data()
recommender = ContentRecommender(job_df)

@router.post("/recommend", tags=["Content-Based Recommendation"])
def recommend_jobs(input_data: SkillInput):
    try:
        user_skills_str = preprocess_skills(input_data.skills)
        results = recommender.recommend(user_skills_str)
        return {"recommendations": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

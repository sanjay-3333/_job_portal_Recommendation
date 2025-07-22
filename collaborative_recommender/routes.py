from fastapi import APIRouter
from .models import InteractionInput, HybridRequest
from .recommender import recommend_jobs_for_user as collab_recommend
from content_recommender.app.recommender import ContentRecommender
from content_recommender.app.services import load_job_data, preprocess_skills

router = APIRouter(
    prefix="/recommend/collab",
    tags=["Collaborative Filtering"]
)

job_df = load_job_data()
content_model = ContentRecommender(job_df)

@router.post("/recommend")
def collab_route(input_data: InteractionInput):
    return collab_recommend(input_data.user_id, input_data.top_n)

@router.post("/recommend/hybrid")
def hybrid_recommend(input_data: HybridRequest):
    print("[DEBUG] hybrid_recommend triggered")
    content_result = content_model.recommend(preprocess_skills(input_data.skills), input_data.top_n)
    print("[DEBUG] Content done")
    collab_result = collab_recommend(input_data.user_id, input_data.top_n)
    print("[DEBUG] Collab done")
    return {
        "hybrid_recommendations": {
            "content_based": content_result,
            "collaborative": collab_result
        }
    }

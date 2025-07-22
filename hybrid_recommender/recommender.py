import pandas as pd
from content_recommender.app.recommender import ContentRecommender
from collaborative_recommender.recommender import recommend_jobs_for_user as collaborative_recs
from content_recommender.app.services import load_job_data

def recommend_hybrid(user_id: int, input_skills: str, top_n: int = 5):
    job_df = load_job_data()

    # Content-Based Filtering
    content_model = ContentRecommender(job_df)
    content = content_model.recommend(input_skills, top_n=20)
    content_df = pd.DataFrame(content)

    # Collaborative Filtering
    collab = collaborative_recs(user_id, top_n=20)
    collab_df = pd.DataFrame(collab)

    # Score Normalization
    if not content_df.empty:
        content_df["content_score"] = 1 - content_df.index / len(content_df)
        content_df.rename(columns={"job_id": "id"}, inplace=True)
    else:
        content_df = pd.DataFrame(columns=["id", "content_score"])

    if not collab_df.empty:
        collab_df["collab_score"] = 1 - collab_df.index / len(collab_df)
        collab_df.rename(columns={"job_id": "id"}, inplace=True)
    else:
        collab_df = pd.DataFrame(columns=["id", "collab_score"])

    # Merge Scores
    hybrid_df = pd.merge(
        content_df[["id", "content_score"]],
        collab_df[["id", "collab_score"]],
        on="id",
        how="outer"
    ).fillna(0)

    hybrid_df["final_score"] = (
        0.6 * hybrid_df["content_score"] + 0.4 * hybrid_df["collab_score"]
    )
    hybrid_df = hybrid_df.sort_values(by="final_score", ascending=False).head(top_n)

    # Merge back with job metadata
    job_df_renamed = job_df.rename(columns={"id": "job_id"})
    result = pd.merge(hybrid_df, job_df_renamed, left_on="id", right_on="job_id", how="left")

    return result[["job_id", "title", "company", "location", "skills"]].to_dict(orient="records")

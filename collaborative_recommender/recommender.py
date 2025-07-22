from .services import (
    load_interaction_data,
    create_user_job_matrix,
    generate_similarity_matrix,
    load_job_metadata
)

def recommend_jobs_for_user(user_id: int, top_n: int = 5):
    interaction_df = load_interaction_data()
    metadata_df = load_job_metadata()

    if interaction_df.empty:
        print("[DEBUG] No interaction data found")
        return []

    matrix = create_user_job_matrix(interaction_df)

    if user_id not in matrix.index:
        print(f"[DEBUG] User {user_id} not found in interaction matrix.")
        return []

    similarity_matrix = generate_similarity_matrix(matrix)
    user_index = matrix.index.get_loc(user_id)

    similarity_scores = list(enumerate(similarity_matrix[user_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]  # Exclude self

    similar_users = [matrix.index[i] for i, _ in similarity_scores]
    job_scores = matrix.loc[similar_users].sum(axis=0)

    interacted_jobs = set(matrix.loc[user_id][matrix.loc[user_id] > 0].index)

    recommended_job_ids = [
        job_id for job_id in job_scores.sort_values(ascending=False).index
        if job_id not in interacted_jobs
    ][:top_n]

    enriched = metadata_df[metadata_df["job_id"].isin(recommended_job_ids)]
    print("[DEBUG] Recommendations generated")
    return enriched.to_dict(orient="records")

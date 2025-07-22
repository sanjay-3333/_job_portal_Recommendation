from collaborative_recommender.app.recommender import recommend_jobs_for_user

def test_recommendation():
    recommendations = recommend_jobs_for_user(user_id=1, top_n=3)
    print("Top 3 recommendations for user 1:", recommendations)
    assert isinstance(recommendations, list)

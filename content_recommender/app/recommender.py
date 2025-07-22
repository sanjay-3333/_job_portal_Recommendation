import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentRecommender:
    def __init__(self, job_df: pd.DataFrame):
        if "skills" not in job_df.columns:
            raise ValueError("Input DataFrame must contain a 'skills' column.")
        self.job_df = job_df.copy()
        self.job_df["skills"] = self.job_df["skills"].fillna("").str.lower()

        self.vectorizer = TfidfVectorizer()
        self.job_vectors = self.vectorizer.fit_transform(self.job_df["skills"])

    def recommend(self, input_skills: str, top_n=5):
        input_vector = self.vectorizer.transform([input_skills.lower()])
        similarity_scores = cosine_similarity(input_vector, self.job_vectors).flatten()
        top_indices = similarity_scores.argsort()[-top_n:][::-1]
        recommendations = self.job_df.iloc[top_indices].to_dict(orient="records")
        return recommendations

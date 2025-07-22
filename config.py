import os

# Get base directory (where config.py is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to jobs.csv inside content_recommender/data/
JOBS_CSV_PATH = os.path.join(BASE_DIR, "content_recommender", "data", "jobs.csv")

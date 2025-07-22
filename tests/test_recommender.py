from fastapi import FastAPI
from content_recommender.routes import router as content_router
import uvicorn

app = FastAPI(
    title="AI-Powered Job Portal",
    description="Resume Parsing + Job Recommendation (Content-Based & Collaborative)",
    version="1.0.0"
)

# Register Routes
app.include_router(content_router, prefix="/recommend/content", tags=["Content-Based Recommendation"])

# Root Route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Portal API"}

# Run App (for local testing)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from content_recommender.app.routes import router as content_router
from collaborative_recommender.routes import router as collab_router
from hybrid_recommender.routes import router as hybrid_router
app = FastAPI(docs_url="/docs", redoc_url=None)

# CORS (Adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static + Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Routers
app.include_router(content_router)
app.include_router(collab_router)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(hybrid_router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.linkedin_routes import router as linkedin_router
from utils.env_helpers import load_env_variables

app = FastAPI()
load_env_variables()
# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(linkedin_router, prefix="/api/linkedin", tags=["LinkedIn"])


@app.get("/")
def read_root():
    return {"message": "🚀 PostAI FastAPI backend is running!"}

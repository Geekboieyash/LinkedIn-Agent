from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.linkedin_routes import router as linkedin_router

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include LinkedIn post routes
app.include_router(linkedin_router, prefix="/api", tags=["LinkedIn"])

@app.get("/")
def read_root():
    return {"message": "🚀 PostAI FastAPI backend is running!"}

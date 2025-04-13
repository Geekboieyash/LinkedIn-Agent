from fastapi import APIRouter
from api.schemas.linkedin import PostRequest, PostResponse
from api.services.linkedin_post import generate_post

router = APIRouter()

@router.post("/generate", response_model=PostResponse)
def generate_linkedin_post(payload: PostRequest):
    content = generate_post(payload.topic)
    return PostResponse(content=content)

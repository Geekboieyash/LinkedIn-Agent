from fastapi import APIRouter, HTTPException
from api.schemas.linkedin import PostRequest, PostResponse
from api.services.linkedin_post import LinkedInPostGenerator
from ai_core.gemini import GeminiModel
from utils.env_helpers import validate_api_key
from utils.logger import logger

router = APIRouter()

@router.post("/generate", response_model=PostResponse)
def generate_linkedin_post(payload: PostRequest):
    try:
        logger.debug(f"Received topic: {payload.topic}")
        api_key = validate_api_key("GEMINI_API_KEY")
        logger.debug(f"API Key Loaded: {bool(api_key)}")
        
        if not api_key:
            raise HTTPException(status_code=500, detail="GEMINI_API_KEY not found in environment variables.")

        model = GeminiModel(api_key=api_key)
        post_generator = LinkedInPostGenerator(model=model)

        topic = payload.topic
        if not topic or not topic.strip():
            logger.warning("Empty topic provided.")
            raise HTTPException(status_code=400, detail="Topic cannot be empty.")

        content = post_generator.generate_post_from_code(topic)
        logger.debug(f"Generated content: {content}")

        if not content:
            logger.error("Post generation returned empty content.")
            raise HTTPException(status_code=500, detail="Failed to generate post content.")

        return PostResponse(content=content)

    except HTTPException as http_exc:
        logger.error(f"HTTP error: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        logger.exception("Unexpected error during post generation.")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
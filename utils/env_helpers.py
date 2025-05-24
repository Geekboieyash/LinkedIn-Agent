import os
from dotenv import load_dotenv
from utils.logger import logger

def load_env_variables():
    """Load environment variables from .env file, or create a default one if not present."""
    if not os.path.exists('.env'):
        logger.warning(".env file not found. Creating one with placeholder keys...")
        with open('.env', 'w') as f:
            f.write("GEMINI_API_KEY=your_api_key_here\n")
        logger.info("✅ .env file created. Please edit it and add your actual GEMINI_API_KEY.")
    
    load_dotenv()
    logger.debug("✅ Environment variables loaded.")

def validate_api_key(env_var_name: str) -> str | None:
    """Validate and clean the API key from the environment"""
    api_key = os.getenv(env_var_name)
    if not api_key or api_key == "your_api_key_here":
        logger.error(f"{env_var_name} not set in .env file.")
        logger.error(f"Please set it in your .env file like this:\n{env_var_name}=your_actual_api_key")
        logger.debug("API Key Loaded: False")
        return None

    
    if api_key.startswith('"') and api_key.endswith('"'):
        logger.warning(f"⚠️ Quotes detected in {env_var_name}, removing them.")
        logger.warning(f"✅ Use this instead: {env_var_name}=your_actual_api_key (no quotes)")
        api_key = api_key[1:-1]

    logger.debug(f"{env_var_name} Loaded Successfully")
    return api_key

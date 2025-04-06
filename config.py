import os
from utils.env_helpers import load_env_variables, validate_api_key

def configure_app(app):
    """Configure the Flask application"""
    # Load environment variables
    load_env_variables()
    
    # Get and validate API key
    api_key = validate_api_key()
    
    # Add API key to app config
    app.config['GOOGLE_API_KEY'] = api_key
    
    return app
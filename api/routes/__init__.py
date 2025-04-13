from .linkedin_routes import generate_linkedin_post

def register_routes(app):
    """Register all application routes"""
    generate_linkedin_post(app)

__all__ = ['register_routes']
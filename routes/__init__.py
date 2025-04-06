from .linkedin_routes import register_linkedin_routes

def register_routes(app):
    """Register all application routes"""
    register_linkedin_routes(app)

__all__ = ['register_routes']
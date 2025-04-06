from flask import Flask
from config import configure_app
from routes import register_routes

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    configure_app(app)
    
    # Register routes
    register_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
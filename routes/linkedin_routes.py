from flask import request, jsonify, render_template
from services import LinkedInPostGenerator
from models.gemini import GeminiModel

def register_linkedin_routes(app):
    """Register routes for LinkedIn post generation"""
    
    @app.route('/')
    def index():
        """Render the main page"""
        return render_template('index.html')
    
    @app.route('/generate', methods=['POST'])
    def generate_post():
        """Generate LinkedIn post based on code input"""
        # Get API key from app config
        api_key = app.config.get('GOOGLE_API_KEY')
        
        # Check if API key is valid
        if not api_key or api_key == "your_api_key_here":
            return jsonify({
                "error": "Google API key not configured. Please check your .env file.",
                "success": False
            }), 500
        
        # Get code from request
        data = request.json
        code = data.get('code', '')
        
        if not code:
            return jsonify({"error": "No code provided"}), 400
        
        # Initialize model and service
        model = GeminiModel(api_key)
        service = LinkedInPostGenerator(model)
        
        # Generate post
        post, error = service.generate_post_from_code(code)
        
        if error:
            return jsonify({
                "error": error,
                "success": False
            }), 500
        
        return jsonify({
            "post": post,
            "success": True
        })
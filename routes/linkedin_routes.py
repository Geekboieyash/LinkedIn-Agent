from flask import request, jsonify, render_template
from services import LinkedInPostGenerator
#from models import gemini



import google.generativeai as genai

class GeminiModel:
    """Interface for Gemini AI model"""
    
    def __init__(self, api_key):
        """Initialize the Gemini model with API key"""
        self.api_key = api_key
        self.model = self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the Gemini model with error handling"""
        try:
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel(model_name="gemini-2.0-flash")
            print("Successfully initialized Gemini 2.0 Flash model")
            return model
        except Exception as e:
            print(f"Error initializing Gemini model: {e}")
            print("The application will start, but AI features won't work until this is fixed.")
            return self._create_placeholder_model()
    
    def _create_placeholder_model(self):
        """Create a placeholder model when initialization fails"""
        class PlaceholderModel:
            def generate_content(self, prompt):
                class ErrorResponse:
                    text = "Error: Could not initialize Gemini model. Please check your API key."
                return ErrorResponse()
        return PlaceholderModel()
    
    def generate_content(self, prompt):
        """Generate content using the Gemini model"""
        return self.model.generate_content(prompt)
    




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
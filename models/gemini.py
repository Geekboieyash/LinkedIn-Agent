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
    


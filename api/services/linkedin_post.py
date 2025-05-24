from ai_core.gemini import GeminiModel
from utils.logger import logger

class LinkedInPostGenerator:
    """Service for generating LinkedIn posts"""
  

    def __init__(self, model: GeminiModel):  
        self.model = model
        logger.debug("✅ LinkedInPostGenerator initialized with GeminiModel.")
    
    def generate_post_from_code(self, code: str) -> str:
        if not code:
            raise ValueError("No code provided")
    
        prompt = f"""
        Create an engaging, professional LinkedIn post about the following code:
        ```
        {code}
        ```
        The post should:  
        1. **Start with an attention-grabbing opening**  
        2. **Explain what the code does** in a simple way  
        3. **Break down the core logic** step by step  
        4. **Highlight real-world applications**  
        5. **Showcase technical strengths**  
        6. **Make the post scannable**  
        7. **End with a compelling call to action**  
        8. **Include 4-5 relevant hashtags**  
    
        ### **Formatting Guidelines:**  
        - Conversational yet professional tone  
        - Use emojis sparingly  
        - Keep it within 300–400 words  
        - Break long explanations into bullets or short paragraphs  
        """
    
        try:
            response = self.model.generate_content(prompt)
            return response.text  # ✅ Just return the string
        except Exception as e:
            error_message = str(e)
            if "API key not valid" in error_message or "invalid api key" in error_message.lower():
                raise RuntimeError("Invalid Google API key. Please check your .env file and ensure you've added a valid Gemini API key.")
            raise RuntimeError(f"Post generation failed: {error_message}")

class LinkedInPostGenerator:
    """Service for generating LinkedIn posts"""
    
    def __init__(self, ai_model):
        """Initialize with AI model"""
        self.ai_model = ai_model
    
    def generate_post_from_code(self, code):
        """Generate a LinkedIn post based on code"""
        if not code:
            return None, "No code provided"
        
        # Prompt for the AI
        prompt = f"""
        Create an engaging, professional LinkedIn post about the following Python code:
        ```
        {code}
        ```
        The post should:  
        1. **Start with an attention-grabbing opening** – a thought-provoking question or a bold statement related to the problem the code solves.  
        2. **Explain what the code does** in a way that appeals to both technical and non-technical audiences.  
        3. **Break down the core logic** step by step, focusing on how it efficiently solves the problem.  
        4. **Highlight real-world applications** where this approach is useful (e.g., social networks, cybersecurity, finance, infrastructure).  
        5. **Showcase technical strengths**, such as algorithmic efficiency, data structures used, and why the chosen approach is effective.  
        6. **Make the post scannable** with short paragraphs, bullet points, and emojis where relevant to improve readability.  
        7. **End with a compelling call to action** (e.g., "Where else do you see this being useful?" or "How would you improve this approach?").  
        8. **Include 4-5 relevant hashtags** for reach and engagement (e.g., #Python #GraphTheory #Algorithms #Tech).  
        
        ### **Formatting Guidelines:**  
        - **Conversational yet professional tone**  
        - **Use emojis sparingly** to enhance readability and engagement  
        - **Keep it within 300-400 words** for optimal LinkedIn engagement  
        - **Break long explanations into bullet points or short paragraphs**  
        """
        
        try:
            # Generate content using the AI model
            response = self.ai_model.generate_content(prompt)
            return response.text, None
        except Exception as e:
            error_message = str(e)
            if "API key not valid" in error_message or "invalid api key" in error_message.lower():
                error_message = "Invalid Google API key. Please check your .env file and ensure you've added a valid Gemini API key."
            return None, error_message
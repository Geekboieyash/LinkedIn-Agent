import os
from dotenv import load_dotenv

def load_env_variables():
    """Load environment variables from .env file"""
    if not os.path.exists('.env'):
        print("Warning: .env file not found.")
        print("Creating .env file with placeholder API key...")
        with open('.env', 'w') as f:
            f.write('GOOGLE_API_KEY=your_api_key_here\n')
        print("Please edit the .env file to add your Google API key.")
    
    load_dotenv()

def validate_api_key():
    """Validate and clean the API key"""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Handle common API key issues
    if not api_key or api_key == "your_api_key_here":
        print("Error: Google API key not set in .env file.")
        print("Please edit the .env file to add your Google API key.")
        print("Example: GOOGLE_API_KEY=your_actual_api_key")
    
    # Remove quotes if they exist (common mistake in .env files)
    if api_key and api_key.startswith('"') and api_key.endswith('"'):
        print("Warning: Removing quotes from API key in .env file.")
        print("For future reference, your .env file should contain:")
        print("GOOGLE_API_KEY=your_actual_api_key")
        print("Not:")
        print('GOOGLE_API_KEY="your_actual_api_key"')
        api_key = api_key[1:-1]  # Remove first and last character (the quotes)
    
    return api_key
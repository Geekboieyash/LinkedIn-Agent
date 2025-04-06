import sys
from dotenv import load_dotenv

import os

def main():
    """Main function to run the application"""
    print("\nStarting LinkedIn Post Generator...")
    print("Access the application at: http://127.0.0.1:5000/")
    try:
        from app import create_app
        app = create_app()
        app.run(debug=True)
    except Exception as e:
        print(f"\nError starting the application: {e}")
        print("Please check your configuration and try again.")


if __name__ == "__main__":
    main()
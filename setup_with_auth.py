#!/usr/bin/env python3
"""
Setup script for Resume ATS Application with Authentication
This script will automatically install all requirements and start the application.
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python 3.7+ is installed"""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_requirements():
    """Install all required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    if not os.path.exists('.env'):
        print("🔧 Creating .env file...")
        with open('.env', 'w') as f:
            f.write('COHERE_API_KEY=O4eGrIMf4vqxiaCHSnYKBYsqNQkf9swh1cUWk2Hj\n')
        print("✅ .env file created!")
    else:
        print("✅ .env file already exists!")

def initialize_database():
    """Initialize the user database"""
    print("🗄️ Initializing user database...")
    try:
        from database import UserDatabase
        db = UserDatabase()
        print("✅ Database initialized successfully!")
        
        # Create a demo user
        success, message = db.create_user("demo_user", "demo@example.com", "demo123")
        if success:
            print("✅ Demo user created (username: demo_user, password: demo123)")
        else:
            print(f"ℹ️ Demo user already exists or creation failed: {message}")
        
        return True
    except Exception as e:
        print(f"❌ Error initializing database: {e}")
        return False

def run_demo():
    """Run the authentication demo"""
    print("🎮 Running authentication demo...")
    try:
        subprocess.run([sys.executable, "demo_auth.py"])
        return True
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        return False

def start_application():
    """Start the Streamlit application with authentication"""
    print("🚀 Starting the Resume ATS Application with Authentication...")
    print("📱 The application will open in your browser automatically.")
    print("🌐 If it doesn't open, go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    print("🔐 Authentication Features:")
    print("   • User registration and login")
    print("   • Secure password storage")
    print("   • User profile management")
    print("   • Session management")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app_with_auth.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

def main():
    """Main setup function"""
    print("🎯 Resume ATS Application with Authentication Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Create .env file
    create_env_file()
    
    # Initialize database
    if not initialize_database():
        print("⚠️ Database initialization failed, but continuing...")
    
    # Ask user if they want to run demo
    print("\n" + "=" * 50)
    choice = input("Would you like to run the authentication demo? (y/n): ").lower().strip()
    if choice in ['y', 'yes']:
        run_demo()
    
    print("\n" + "=" * 50)
    choice = input("Start the application now? (y/n): ").lower().strip()
    if choice in ['y', 'yes']:
        start_application()
    else:
        print("Setup completed! You can start the application later with:")
        print("streamlit run app_with_auth.py")

if __name__ == "__main__":
    main()

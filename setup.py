#!/usr/bin/env python3
"""
Setup script for Resume ATS Application
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

def start_application():
    """Start the Streamlit application"""
    print("🚀 Starting the application...")
    print("📱 The application will open in your browser automatically.")
    print("🌐 If it doesn't open, go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Application stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

def main():
    """Main setup function"""
    print("🎯 Resume ATS Application Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Create .env file
    create_env_file()
    
    # Start application
    start_application()

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Demo script to test the authentication system
"""

from database import UserDatabase
from auth import AuthManager

def demo_authentication():
    """Demonstrate the authentication system"""
    print("🎯 Resume ATS Authentication System Demo")
    print("=" * 50)
    
    # Initialize database and auth manager
    db = UserDatabase()
    auth = AuthManager()
    
    # Test user creation
    print("\n1. Testing User Creation:")
    print("-" * 30)
    
    test_users = [
        ("john_doe", "john@example.com", "password123"),
        ("jane_smith", "jane@example.com", "securepass456"),
        ("test_user", "test@example.com", "testpass789")
    ]
    
    for username, email, password in test_users:
        success, message = db.create_user(username, email, password)
        if success:
            print(f"✅ Created user: {username}")
        else:
            print(f"❌ Failed to create {username}: {message}")
    
    # Test authentication
    print("\n2. Testing Authentication:")
    print("-" * 30)
    
    test_logins = [
        ("john_doe", "password123"),
        ("jane_smith", "wrongpassword"),
        ("nonexistent_user", "password123")
    ]
    
    for username, password in test_logins:
        success, result = db.authenticate_user(username, password)
        if success:
            print(f"✅ Login successful for: {username}")
            print(f"   User ID: {result['id']}, Email: {result['email']}")
        else:
            print(f"❌ Login failed for {username}: {result}")
    
    # Test user retrieval
    print("\n3. Testing User Retrieval:")
    print("-" * 30)
    
    user = db.get_user_by_username("john_doe")
    if user:
        print(f"✅ Retrieved user: {user['username']}")
        print(f"   Email: {user['email']}")
        print(f"   Created: {user['created_at']}")
    else:
        print("❌ Failed to retrieve user")
    
    # Test password update
    print("\n4. Testing Password Update:")
    print("-" * 30)
    
    success, message = db.update_user_password("john_doe", "password123", "newpassword456")
    if success:
        print("✅ Password updated successfully")
        
        # Test login with new password
        success, result = db.authenticate_user("john_doe", "newpassword456")
        if success:
            print("✅ Login with new password successful")
        else:
            print("❌ Login with new password failed")
    else:
        print(f"❌ Password update failed: {message}")
    
    # Show all users
    print("\n5. All Users in Database:")
    print("-" * 30)
    
    users = db.get_all_users()
    for user in users:
        print(f"👤 {user['username']} ({user['email']}) - Created: {user['created_at']}")
    
    print("\n" + "=" * 50)
    print("Demo completed! You can now run the Streamlit app with authentication.")
    print("Run: streamlit run app_with_auth.py")

if __name__ == "__main__":
    demo_authentication()

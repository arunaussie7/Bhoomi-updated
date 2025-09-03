# 🔐 Authentication System Guide

## Overview

The Resume ATS application now includes a comprehensive authentication system that allows users to:
- Create secure accounts
- Login with username and password
- Manage their profiles
- Access personalized resume analysis features

## Features

### 🔑 User Authentication
- **Secure Registration**: Users can create accounts with username, email, and password
- **Login System**: Secure login with session management
- **Password Security**: Passwords are hashed using SHA-256
- **Session Management**: Automatic session handling with Streamlit

### 👤 User Profile Management
- **Profile Viewing**: View account information and statistics
- **Password Changes**: Update passwords with current password verification
- **Account Deletion**: Secure account deletion with password confirmation

### 🗄️ Database
- **SQLite Database**: Lightweight, file-based database for user storage
- **Secure Storage**: Passwords are never stored in plain text
- **User Data**: Stores username, email, creation date, and last login

## File Structure

```
bhoomi-final-main/
├── app_with_auth.py          # Main application with authentication
├── auth.py                   # Authentication manager and UI components
├── database.py               # Database operations and user management
├── demo_auth.py              # Demo script to test authentication
├── setup_with_auth.py        # Setup script for authenticated version
├── users.db                  # SQLite database (created automatically)
└── AUTHENTICATION_GUIDE.md   # This guide
```

## Quick Start

### 1. Setup and Installation
```bash
# Run the setup script
python3 setup_with_auth.py

# Or manually install dependencies
pip3 install -r requirements.txt
```

### 2. Start the Application
```bash
# Start the application with authentication
streamlit run app_with_auth.py
```

### 3. Access the Application
- Open your browser to `http://localhost:8501`
- You'll see the login/signup page
- Create a new account or use the demo account:
  - **Username**: `demo_user`
  - **Password**: `demo123`

## Usage Guide

### Creating an Account
1. Click on the "📝 Sign Up" tab
2. Fill in the required information:
   - **Username**: 3-20 characters, letters, numbers, and underscores only
   - **Email**: Valid email address format
   - **Password**: Minimum 6 characters
   - **Confirm Password**: Must match the password
3. Click "Sign Up"
4. You'll be redirected to the login page

### Logging In
1. Click on the "🔐 Login" tab
2. Enter your username and password
3. Click "Login"
4. You'll be redirected to the main application

### Using the Application
Once logged in, you can:
- **Resume Analysis**: Upload PDF resumes and analyze them against job descriptions
- **View Results**: See ATS scores, missing keywords, and profile summaries
- **Get Improvement Tips**: Receive personalized suggestions
- **Manage Profile**: Update password or delete account

### Profile Management
1. Navigate to "User Profile" in the sidebar
2. View your account information
3. Change your password (requires current password)
4. Delete your account (requires password confirmation)

## Security Features

### Password Security
- Passwords are hashed using SHA-256
- No plain text passwords are stored
- Password validation ensures minimum security requirements

### Session Security
- Sessions are managed by Streamlit
- Automatic logout on browser close
- Session state is cleared on logout

### Input Validation
- Email format validation
- Username format validation
- Password strength requirements
- SQL injection protection through parameterized queries

## Database Schema

The `users` table contains:
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
```

## Demo and Testing

### Run the Demo
```bash
python3 demo_auth.py
```

This will:
- Create test users
- Test authentication
- Demonstrate all database operations
- Show user management features

### Test Users
The demo creates these test users:
- **Username**: `john_doe`, **Email**: `john@example.com`, **Password**: `password123`
- **Username**: `jane_smith`, **Email**: `jane@example.com`, **Password**: `securepass456`
- **Username**: `test_user`, **Email**: `test@example.com`, **Password**: `testpass789`

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure you have write permissions in the project directory
   - Check if `users.db` file exists and is accessible

2. **Authentication Failed**
   - Verify username and password are correct
   - Check if the user account exists in the database

3. **Session Issues**
   - Clear browser cache and cookies
   - Restart the Streamlit application

4. **Password Update Failed**
   - Ensure current password is correct
   - Check new password meets requirements (6+ characters)

### Reset Database
If you need to reset the user database:
```bash
# Delete the database file
rm users.db

# Restart the application (database will be recreated)
streamlit run app_with_auth.py
```

## API Reference

### AuthManager Class
```python
from auth import AuthManager

auth = AuthManager()

# Check authentication status
is_logged_in = auth.is_authenticated()

# Get current user
user = auth.get_current_user()

# Logout
auth.logout()
```

### UserDatabase Class
```python
from database import UserDatabase

db = UserDatabase()

# Create user
success, message = db.create_user(username, email, password)

# Authenticate user
success, user_data = db.authenticate_user(username, password)

# Get user by username
user = db.get_user_by_username(username)

# Update password
success, message = db.update_user_password(username, old_password, new_password)

# Delete user
success, message = db.delete_user(username, password)
```

## Future Enhancements

Potential improvements for the authentication system:
- Email verification for new accounts
- Password reset functionality
- Two-factor authentication
- User roles and permissions
- Account recovery options
- Login attempt limiting
- Password complexity requirements
- Session timeout management

## Support

If you encounter any issues with the authentication system:
1. Check the troubleshooting section above
2. Run the demo script to test functionality
3. Verify all dependencies are installed correctly
4. Check the console output for error messages

---

**Note**: This authentication system is designed for development and educational purposes. For production use, consider implementing additional security measures such as HTTPS, stronger password hashing (bcrypt), and more robust session management.

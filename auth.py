import streamlit as st
import re
from database import UserDatabase

class AuthManager:
    def __init__(self):
        self.db = UserDatabase()
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_password(self, password):
        """Validate password strength"""
        if len(password) < 6:
            return False, "Password must be at least 6 characters long"
        if len(password) > 50:
            return False, "Password must be less than 50 characters"
        return True, "Password is valid"
    
    def validate_username(self, username):
        """Validate username"""
        if len(username) < 3:
            return False, "Username must be at least 3 characters long"
        if len(username) > 20:
            return False, "Username must be less than 20 characters"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        return True, "Username is valid"
    
    def show_login_form(self):
        """Display login form"""
        st.subheader("🔐 Login")
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submit_button = st.form_submit_button("Login", type="primary")
            
            if submit_button:
                if not username or not password:
                    st.error("Please fill in all fields!")
                    return False
                
                success, result = self.db.authenticate_user(username, password)
                
                if success:
                    st.session_state.authenticated = True
                    st.session_state.user = result
                    st.success(f"Welcome back, {result['username']}!")
                    st.rerun()
                else:
                    st.error(result)
        
        return False
    
    def show_signup_form(self):
        """Display signup form"""
        st.subheader("📝 Create Account")
        
        with st.form("signup_form"):
            username = st.text_input("Username", placeholder="Choose a username")
            email = st.text_input("Email", placeholder="Enter your email address")
            password = st.text_input("Password", type="password", placeholder="Create a password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            submit_button = st.form_submit_button("Sign Up", type="primary")
            
            if submit_button:
                # Validation
                if not all([username, email, password, confirm_password]):
                    st.error("Please fill in all fields!")
                    return False
                
                # Validate username
                username_valid, username_msg = self.validate_username(username)
                if not username_valid:
                    st.error(username_msg)
                    return False
                
                # Validate email
                if not self.validate_email(email):
                    st.error("Please enter a valid email address!")
                    return False
                
                # Validate password
                password_valid, password_msg = self.validate_password(password)
                if not password_valid:
                    st.error(password_msg)
                    return False
                
                # Check password confirmation
                if password != confirm_password:
                    st.error("Passwords do not match!")
                    return False
                
                # Create user
                success, result = self.db.create_user(username, email, password)
                
                if success:
                    st.success("Account created successfully! Please login.")
                    st.session_state.show_login = True
                    st.rerun()
                else:
                    st.error(result)
        
        return False
    
    def show_user_profile(self):
        """Display user profile and account management"""
        if not st.session_state.get('authenticated'):
            return
        
        user = st.session_state.user
        st.subheader(f"👤 Profile - {user['username']}")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"""
            **Username:** {user['username']}  
            **Email:** {user['email']}  
            **User ID:** {user['id']}
            """)
        
        with col2:
            if st.button("🔄 Refresh Profile", type="secondary"):
                updated_user = self.db.get_user_by_username(user['username'])
                if updated_user:
                    st.session_state.user = updated_user
                    st.rerun()
        
        st.markdown("---")
        
        # Change Password Section
        st.subheader("🔒 Change Password")
        with st.form("change_password_form"):
            current_password = st.text_input("Current Password", type="password")
            new_password = st.text_input("New Password", type="password")
            confirm_new_password = st.text_input("Confirm New Password", type="password")
            change_password_button = st.form_submit_button("Change Password", type="primary")
            
            if change_password_button:
                if not all([current_password, new_password, confirm_new_password]):
                    st.error("Please fill in all fields!")
                elif new_password != confirm_new_password:
                    st.error("New passwords do not match!")
                else:
                    password_valid, password_msg = self.validate_password(new_password)
                    if not password_valid:
                        st.error(password_msg)
                    else:
                        success, result = self.db.update_user_password(
                            user['username'], current_password, new_password
                        )
                        if success:
                            st.success(result)
                        else:
                            st.error(result)
        
        st.markdown("---")
        
        # Delete Account Section
        st.subheader("⚠️ Danger Zone")
        with st.form("delete_account_form"):
            st.warning("This action cannot be undone!")
            delete_password = st.text_input("Enter your password to confirm deletion", type="password")
            delete_button = st.form_submit_button("Delete Account", type="secondary")
            
            if delete_button:
                if not delete_password:
                    st.error("Please enter your password to confirm deletion!")
                else:
                    success, result = self.db.delete_user(user['username'], delete_password)
                    if success:
                        st.success(result)
                        # Clear session and redirect to login
                        for key in list(st.session_state.keys()):
                            del st.session_state[key]
                        st.session_state.show_login = True
                        st.rerun()
                    else:
                        st.error(result)
    
    def logout(self):
        """Logout user and clear session"""
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.show_login = True
        st.rerun()
    
    def is_authenticated(self):
        """Check if user is authenticated"""
        return st.session_state.get('authenticated', False)
    
    def get_current_user(self):
        """Get current authenticated user"""
        return st.session_state.get('user', None)

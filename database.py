import sqlite3
import hashlib
import os
from datetime import datetime

class UserDatabase:
    def __init__(self, db_path="users.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create users table if it doesn't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_login TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_user(self, username, email, password):
        """Create a new user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            password_hash = self.hash_password(password)
            cursor.execute('''
                INSERT INTO users (username, email, password_hash)
                VALUES (?, ?, ?)
            ''', (username, email, password_hash))
            
            conn.commit()
            return True, "User created successfully!"
        except sqlite3.IntegrityError as e:
            if "username" in str(e):
                return False, "Username already exists!"
            elif "email" in str(e):
                return False, "Email already exists!"
            else:
                return False, "Database error occurred!"
        except Exception as e:
            return False, f"Error creating user: {str(e)}"
        finally:
            conn.close()
    
    def authenticate_user(self, username, password):
        """Authenticate user login"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            password_hash = self.hash_password(password)
            cursor.execute('''
                SELECT id, username, email FROM users 
                WHERE username = ? AND password_hash = ?
            ''', (username, password_hash))
            
            user = cursor.fetchone()
            
            if user:
                # Update last login time
                cursor.execute('''
                    UPDATE users SET last_login = CURRENT_TIMESTAMP 
                    WHERE id = ?
                ''', (user[0],))
                conn.commit()
                
                return True, {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2]
                }
            else:
                return False, "Invalid username or password!"
                
        except Exception as e:
            return False, f"Authentication error: {str(e)}"
        finally:
            conn.close()
    
    def get_user_by_username(self, username):
        """Get user information by username"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                SELECT id, username, email, created_at, last_login FROM users 
                WHERE username = ?
            ''', (username,))
            
            user = cursor.fetchone()
            if user:
                return {
                    'id': user[0],
                    'username': user[1],
                    'email': user[2],
                    'created_at': user[3],
                    'last_login': user[4]
                }
            return None
                
        except Exception as e:
            return None
        finally:
            conn.close()
    
    def update_user_password(self, username, old_password, new_password):
        """Update user password"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            # First verify old password
            old_password_hash = self.hash_password(old_password)
            cursor.execute('''
                SELECT id FROM users 
                WHERE username = ? AND password_hash = ?
            ''', (username, old_password_hash))
            
            if not cursor.fetchone():
                return False, "Current password is incorrect!"
            
            # Update to new password
            new_password_hash = self.hash_password(new_password)
            cursor.execute('''
                UPDATE users SET password_hash = ? 
                WHERE username = ?
            ''', (new_password_hash, username))
            
            conn.commit()
            return True, "Password updated successfully!"
            
        except Exception as e:
            return False, f"Error updating password: {str(e)}"
        finally:
            conn.close()
    
    def delete_user(self, username, password):
        """Delete user account"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            password_hash = self.hash_password(password)
            cursor.execute('''
                DELETE FROM users 
                WHERE username = ? AND password_hash = ?
            ''', (username, password_hash))
            
            if cursor.rowcount > 0:
                conn.commit()
                return True, "Account deleted successfully!"
            else:
                return False, "Invalid credentials or user not found!"
                
        except Exception as e:
            return False, f"Error deleting account: {str(e)}"
        finally:
            conn.close()
    
    def get_all_users(self):
        """Get all users (for admin purposes)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                SELECT id, username, email, created_at, last_login FROM users 
                ORDER BY created_at DESC
            ''')
            
            users = cursor.fetchall()
            return [{
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'created_at': user[3],
                'last_login': user[4]
            } for user in users]
                
        except Exception as e:
            return []
        finally:
            conn.close()

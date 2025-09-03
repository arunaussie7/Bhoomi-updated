# 🎯 Smart Resume ATS with Authentication System

A sophisticated Application Tracking System (ATS) built with Streamlit and Cohere AI, featuring a complete user authentication system for secure resume analysis and optimization.

## 🌟 Features

### 🔐 Authentication System
- **User Registration & Login**: Secure signup and login with username, email, and password
- **Password Security**: SHA-256 hashed passwords with validation
- **Session Management**: Automatic session handling with Streamlit
- **User Profile Management**: View account info, change passwords, delete accounts
- **SQLite Database**: Lightweight, file-based database for user storage

### 📊 Resume Analysis
- **ATS Score Calculation**: Get accurate percentage match with job descriptions
- **Keyword Analysis**: Identify missing keywords to improve your resume
- **Profile Summary**: Receive comprehensive profile summaries
- **PDF Processing**: Upload and analyze PDF resumes
- **Improvement Suggestions**: Personalized recommendations for resume enhancement

### 🛠️ Technical Features
- **Cohere AI Integration**: Advanced AI-powered text analysis
- **Streamlit UI**: Modern, responsive web interface
- **Database Management**: SQLite for persistent user data
- **Error Handling**: Comprehensive validation and error messages
- **Documentation**: Complete setup and usage guides

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Internet connection
- Cohere API key (free at [cohere.ai](https://cohere.ai))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/arunaussie7/Bhoomi-updated.git
   cd Bhoomi-updated
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment**
   ```bash
   # Create .env file with your Cohere API key
   echo "COHERE_API_KEY=your_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run app_with_auth.py
   ```

5. **Access the application**
   - Open your browser to `http://localhost:8501`
   - Create an account or use test credentials

## 📁 Project Structure

```
Bhoomi-updated/
├── app_with_auth.py          # Main application with authentication
├── auth.py                   # Authentication manager and UI components
├── database.py               # Database operations and user management
├── demo_auth.py              # Demo script to test authentication
├── setup_with_auth.py        # Setup script for authenticated version
├── app.py                    # Original application without authentication
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create this)
├── users.db                  # SQLite database (created automatically)
├── AUTHENTICATION_GUIDE.md   # Complete authentication documentation
├── INSTALLATION_GUIDE.txt    # Detailed installation instructions
└── README.md                 # This file
```

## 🔑 Test Accounts

For testing purposes, you can use these pre-created accounts:

| Username | Email | Password |
|----------|-------|----------|
| `john_doe` | `john@example.com` | `password123` |
| `jane_smith` | `jane@example.com` | `securepass456` |
| `test_user` | `test@example.com` | `testpass789` |

## 🎮 Demo

Run the authentication demo to test the system:

```bash
python demo_auth.py
```

This will:
- Create test users
- Test authentication
- Demonstrate all database operations
- Show user management features

## 📖 Usage Guide

### 1. Creating an Account
1. Click on the "📝 Sign Up" tab
2. Fill in username, email, and password
3. Click "Sign Up"
4. You'll be redirected to the login page

### 2. Logging In
1. Click on the "🔐 Login" tab
2. Enter your credentials
3. Click "Login"
4. Access the main application

### 3. Resume Analysis
1. Navigate to "Resume Analysis"
2. Upload your PDF resume
3. Paste the job description
4. Click "Submit"
5. View results in "Analysis Results"

### 4. Profile Management
1. Go to "User Profile" in the sidebar
2. View account information
3. Change password or delete account

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
COHERE_API_KEY=your_cohere_api_key_here
```

### Database
The application uses SQLite for user storage. The database file (`users.db`) is created automatically on first run.

## 🛡️ Security Features

- **Password Hashing**: SHA-256 encryption
- **Input Validation**: Email format, username format, password strength
- **Session Security**: Automatic logout and session management
- **SQL Injection Protection**: Parameterized queries
- **File Upload Security**: PDF validation and processing

## 📚 Documentation

- **[Authentication Guide](AUTHENTICATION_GUIDE.md)**: Complete authentication system documentation
- **[Installation Guide](INSTALLATION_GUIDE.txt)**: Detailed setup instructions
- **[Project Documentation](PROJECT_DOCUMENTATION.md)**: Technical specifications

## 🚀 Deployment

### Local Development
```bash
streamlit run app_with_auth.py
```

### Production Deployment
For production deployment, consider:
- Using a production WSGI server
- Setting up HTTPS
- Using a more robust database (PostgreSQL)
- Implementing stronger password hashing (bcrypt)
- Adding rate limiting and security headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Bhoomika Vishwanath** - *Initial work* - [GitHub](https://github.com/praj2408/End-To-End-Resume-ATS-Tracking-LLM-Project-With-Google-Gemini-Pro)
- **Arun Aussie** - *Authentication System & Updates* - [GitHub](https://github.com/arunaussie7)

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - Web application framework
- [Cohere AI](https://cohere.ai/) - AI-powered text analysis
- [PyPDF2](https://pypdf2.readthedocs.io/) - PDF processing
- [SQLite](https://www.sqlite.org/) - Database management

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section in the documentation
2. Run the demo script to test functionality
3. Verify all dependencies are installed correctly
4. Check the console output for error messages
5. Open an issue on GitHub

---

**Made with ❤ by Bhoomika Vishwanath and enhanced by Arun Aussie**
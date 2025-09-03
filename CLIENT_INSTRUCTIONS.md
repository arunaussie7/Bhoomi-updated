# 🎯 Resume ATS Application - Client Instructions

## 🚀 Quick Start (Choose Your Operating System)

### For Windows Users:
1. **Double-click** `start_app.bat` file
2. Wait for installation to complete
3. The application will open automatically in your browser

### For Mac/Linux Users:
1. **Double-click** `start_app.sh` file
2. Wait for installation to complete
3. The application will open automatically in your browser

---

## 📋 Manual Setup (If automatic setup doesn't work)

### Prerequisites:
- Python 3.7 or higher installed on your computer

### Step-by-Step Instructions:

#### Step 1: Open Terminal/Command Prompt
- **Windows**: Press `Win + R`, type `cmd`, press Enter
- **Mac**: Press `Cmd + Space`, type `Terminal`, press Enter
- **Linux**: Press `Ctrl + Alt + T`

#### Step 2: Navigate to Project Folder
```bash
cd "path/to/your/project/folder"
```

#### Step 3: Run Setup Script
```bash
python setup.py
```

#### Step 4: Alternative Manual Commands
If the setup script doesn't work, run these commands one by one:

```bash
# Install requirements
pip install -r requirements.txt

# Start the application
streamlit run app.py
```

---

## 🌐 Accessing the Application

Once started, the application will be available at:
- **Local URL**: http://localhost:8501
- **Network URL**: http://your-ip-address:8501

---

## 📱 How to Use the Application

### 1. Resume Analysis Page
- Upload your PDF resume
- Paste the job description
- Click "Submit"
- Wait for analysis to complete

### 2. Analysis Results Page
- View your ATS match score
- See missing keywords
- Read your profile summary
- Click "Resume Improvement Tips"

### 3. Improvement Tips Page
- Get personalized suggestions
- View keywords to include
- Click "Generate Detailed Improvement Plan"

### 4. Detailed Improvement Plan Page
- Read comprehensive improvement suggestions
- Follow the recommendations to improve your resume

---

## ⚠️ Troubleshooting

### If you get "Python not found" error:
1. Download Python from https://python.org
2. Install it with "Add to PATH" option checked
3. Restart your computer
4. Try running the setup again

### If you get "pip not found" error:
1. Try using: `python -m pip install -r requirements.txt`
2. Or: `python3 -m pip install -r requirements.txt`

### If the browser doesn't open automatically:
1. Open your web browser
2. Go to: http://localhost:8501

### If you get permission errors (Mac/Linux):
1. Make the script executable: `chmod +x start_app.sh`
2. Then run: `./start_app.sh`

---

## 🛑 Stopping the Application

- Press `Ctrl + C` in the terminal/command prompt
- Or close the terminal window

---

## 📞 Support

If you encounter any issues:
1. Check that Python 3.7+ is installed
2. Ensure you have internet connection
3. Try running the manual commands
4. Contact the developer for assistance

---

## 📁 Files Included

- `app.py` - Main application
- `setup.py` - Automatic setup script
- `start_app.bat` - Windows startup file
- `start_app.sh` - Mac/Linux startup file
- `requirements.txt` - Required packages
- `CLIENT_INSTRUCTIONS.md` - This file

---

**🎉 That's it! Your Resume ATS application is ready to use!** 
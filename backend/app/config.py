import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://devuser:devpassword@localhost:5432/social_media_dev"
)

# FastAPI settings
DEBUG = os.getenv("DEBUG", "True") == "True"

# JWT settings
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

# CORS settings
CORS_ORIGINS = [
    "http://localhost:3000",  # Next.js development
    "http://localhost:8000",  # FastAPI development
]

# Email settings (for OTP - we'll implement later)
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# Google OAuth
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")

# GitHub OAuth
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "Ov23liEasK0L3pqRe3pn")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "a9c825866b600620f9b5e39d791c8e6c413095fe")
GITHUB_REDIRECT_URI = os.getenv("GITHUB_REDIRECT_URI", "http://localhost:8000/api/v1/oauth/github/callback")

# Frontend URL (used to redirect back after OAuth completes)
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# App settings
APP_NAME = "Social Media API"
APP_VERSION = "0.1.0"

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
SMTP_FROM_NAME = os.getenv("SMTP_FROM_NAME", "Social Media App")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI", "http://localhost:8000/api/v1/oauth/google/callback")

import os
from os import environ

# Load .env file if present (local development)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

API_ID = int(environ.get("API_ID", 0) or 0)
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", 0) or 0)
CREDIT = environ.get("CREDIT", '𝐂𝐋𝐀𝐓 𝐎𝐖𝐍𝐄𝐑')
CREDIT_LINK = environ.get("CREDIT_LINK", 'https://t.me/CLAT_OWNER')
UPGRADE_TEXT = environ.get("UPGRADE_TEXT", "")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

# MongoDB Configuration
MONGO_URL = environ.get("MONGO_URL", "")
DATABASE_NAME = environ.get("DATABASE_NAME", "eagle")

# Owner and Admin Configuration
OWNER_ID = int(environ.get("OWNER_ID", 0) or 0)
OWNER_ID2 = int(environ.get("OWNER_ID2", 0) or 0)
ADMINS = [OWNER_ID, OWNER_ID2]  # Can be extended via environment
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


# ── Startup validation ────────────────────────────────────────────────────────
_missing = []
if not API_ID:
    _missing.append("API_ID")
if not API_HASH:
    _missing.append("API_HASH")
if not BOT_TOKEN:
    _missing.append("BOT_TOKEN")
if not MONGO_URL:
    _missing.append("MONGO_URL")
if _missing:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(_missing)}\n"
        "Copy .env.example to .env and fill in the values."
    )

# ── API endpoints ─────────────────────────────────────────────────────────────
api_url = "http://master-api-v3.vercel.app/"
api_token = environ.get("API_TOKEN", "")
token_cp = environ.get("TOKEN_CP", "")
adda_token = environ.get("ADDA_TOKEN", "")
photologo = 'https://i.ibb.co/zTPJFct8/photo-2025-04-25-12-55-01-7497233558289776672.jpg' #https://envs.sh/GV0.jpg
photoyt = 'https://i.ibb.co/zTPJFct8/photo-2025-04-25-12-55-01-7497233558289776672.jpg' #https://envs.sh/GVi.jpg
photocp = 'https://i.ibb.co/zTPJFct8/photo-2025-04-25-12-55-01-7497233558289776672.jpg'
photozip = 'https://i.ibb.co/zTPJFct8/photo-2025-04-25-12-55-01-7497233558289776672.jpg'
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.

# Message Templates for Authentication
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>

Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name : {name}
🆔 USER ID : {user_id}
📅 EXPIRY : {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully !</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}


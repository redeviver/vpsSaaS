# backend/auth.py
import jwt
from datetime import datetime, timedelta

SECRET = "supersecret"

def generate_token(user):
    payload = {
        "user": user,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

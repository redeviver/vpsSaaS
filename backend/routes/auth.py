from fastapi import APIRouter, HTTPException
from database import SessionLocal
from models import User
from auth import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/register")
def register(data: dict):
    db = SessionLocal()

    user = User(
        email=data["email"],
        password=hash_password(data["password"])
    )

    db.add(user)
    db.commit()

    return {"msg": "created"}

@router.post("/login")
def login(data: dict):
    db = SessionLocal()

    user = db.query(User).filter(User.email == data["email"]).first()

    if not user or not verify_password(data["password"], user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user_id": user.id})

    return {"access_token": token}

from fastapi import APIRouter

router = APIRouter()

@router.get("/vpn/status")
def status():
    return {"status": "active"}

from fastapi import APIRouter

router = APIRouter()

@router.get("/dream")
def get_dream():
    return {"message": "Dream route working:"}

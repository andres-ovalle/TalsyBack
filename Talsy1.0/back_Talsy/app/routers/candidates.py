from fastapi import APIRouter
from services.candidate_service import get_all_candidates

router = APIRouter()

@router.get("/")
def list_candidates():
    return get_all_candidates()

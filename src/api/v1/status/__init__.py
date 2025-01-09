from fastapi import APIRouter

router = APIRouter(
    prefix="/status",
    
)

from src.api.v1.status.status import get_status
from fastapi import status
from fastapi.responses import JSONResponse
from . import router

@router.get("")
async def get_status():
    return JSONResponse(content={"status": "ok"}, status_code=status.HTTP_200_OK)
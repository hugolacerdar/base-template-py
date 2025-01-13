from fastapi import Depends

from src.api.dependencies import resolve_get_system_status_use_case
from src.api.v1.status.status_response import StatusResponse

from . import router


@router.get("", response_model=StatusResponse)
async def get_status(
    get_system_status_use_case=Depends(resolve_get_system_status_use_case)
):
    status = await get_system_status_use_case.execute()

    return StatusResponse(
        updated_at=status['updated_at'],
        dependencies=status['dependencies']
    )
    

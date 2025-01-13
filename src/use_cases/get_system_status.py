from datetime import datetime

from src.infra.data.repository.abc import Repository


class GetSystemStatus:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def execute(self):
        database_status = await self.repository.get_database_status()
        updated_at = datetime.now()
        return {
            "updated_at": updated_at,
            "dependencies": {
                "database": database_status
            }
        }
from datetime import datetime

from src.infra.data.repository.abc import Repository


class GetSystemStatus:
	def __init__(self, repository: Repository) -> None:
		self.repository = repository

	async def execute(self) -> dict[str, datetime | dict[str, dict[str, str | int]]]:
		database_status: dict[str, str | int] = await self.repository.get_database_status()
		updated_at: datetime = datetime.now()
		return {'updated_at': updated_at, 'dependencies': {'database': database_status}}

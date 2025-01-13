from asyncpg import Pool  # type: ignore

from src.infra.data.database.abc import Database
from src.infra.data.database.pg_database import PostgresDatabase
from src.infra.data.repository.abc import Repository


class PostgresRepository(Repository):
	def __init__(self, database: Database) -> None:
		if not isinstance(database, PostgresDatabase):
			raise ValueError(f'Invalid database type. Expected PostgresDatabase, got {type(database)}')

		self.database: PostgresDatabase = database

	async def get_database_status(self) -> dict[str, int | str]:
		pool: Pool = await self.database.get_pool()
		async with pool.acquire() as conn:  # type: ignore
			version: str = await conn.fetchval('SELECT version();')  # type: ignore
			max_connections: int = await conn.fetchval('SHOW max_connections;')  # type: ignore
			active_connections: int = await conn.fetchval('SELECT COUNT(*)::int FROM pg_stat_activity WHERE datname = current_database();')  # type: ignore

		return {
			'version': version,
			'max_connections': max_connections,
			'active_connections': active_connections,
		}

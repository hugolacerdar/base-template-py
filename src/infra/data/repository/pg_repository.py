from asyncpg import Pool

from src.infra.data.database.abc import Database
from src.infra.data.database.pg_database import PostgresDatabase
from src.infra.data.repository.abc import Repository


class PostgresRepository(Repository):
	def __init__(self, database: Database) -> None:
		if not isinstance(database, PostgresDatabase):
			raise ValueError(f'Invalid database type. Expected PostgresDatabase, got {type(database)}')

		self.database: PostgresDatabase = database

	async def get_database_status(self) -> dict:
		pool: Pool = await self.database.get_pool()
		async with pool.acquire() as conn:
			version = await conn.fetchval('SELECT version();')
			max_connections = await conn.fetchval('SHOW max_connections;')
			active_connections = await conn.fetchval('SELECT COUNT(*)::int FROM pg_stat_activity WHERE datname = current_database();')

		return {
			'version': version,
			'max_connections': max_connections,
			'active_connections': active_connections,
		}

import asyncpg

from src.infra.data.database.abc import Database


class PostgresDatabase(Database):
	def __init__(self, user: str, password: str, host: str, port: int, database: str):
		self.__user = user
		self.__password = password
		self.__host = host
		self.__port = port
		self.__database = database
		self.__pool: asyncpg.Pool | None = None

	async def get_pool(self) -> asyncpg.Pool:
		if not self.__pool:
			self.__pool = await asyncpg.create_pool(
				user=self.__user,
				password=self.__password,
				host=self.__host,
				port=self.__port,
				database=self.__database,
			)
		return self.__pool

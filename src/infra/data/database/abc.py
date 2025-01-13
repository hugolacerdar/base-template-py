from abc import ABC, abstractmethod
from typing import Any


class Database(ABC):
	@abstractmethod
	async def get_pool(self) -> Any:
		"""
		Returns the database connection or pool.
		"""
		pass

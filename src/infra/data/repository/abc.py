from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    async def get_database_status(self) -> dict:
        """
        Returns database status information, such as version and connection stats.
        """
        pass
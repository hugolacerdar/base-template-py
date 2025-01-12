from fastapi import Depends
from src.infra.data.repository.abc import Repository
from src.infra.data.repository.pg_repository import PostgresRepository
from src.infra.data.database.abc import Database
from src.infra.data.database.pg_database import PostgresDatabase
from src.environment import settings
from src.use_cases.get_system_status import GetSystemStatus

def resolve_database():
    return PostgresDatabase(
        user=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port,
        database=settings.db_name,
    )

def resolve_repository(database: Database=Depends(resolve_database)):
    return PostgresRepository(
        database=database
    )

def resolve_get_system_status_use_case(repository: Repository=Depends(resolve_repository)):
    return GetSystemStatus(repository=repository)
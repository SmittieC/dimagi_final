from pydantic.env_settings import BaseSettings

class BaseConfig(BaseSettings):
    DATABASE_URL: str = "postgres://dimagi:dev@localhost/backend"

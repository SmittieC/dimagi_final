from pydantic.env_settings import BaseSettings


class BaseConfig(BaseSettings):
    DATABASE_URL: str = "postgresql://dimagi:dev@localhost/backend"


Config = BaseConfig()

from pydantic.env_settings import BaseSettings


class BaseConfig(BaseSettings):
    DATABASE_URL: str = "postgresql://dimagi:dev@localhost/backend"
    SERVER_URL: str = "http://localhost:8000"
    GEOCODER_API_KEY: str = "dev-key"
    ADMIN_EMAIL: str = "admin"
    ADMIN_PASSWORD: str = "admin"


Config = BaseConfig()

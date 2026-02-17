from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Validamos que existan estas variables en el .env
    DATABASE_URL: str
    
    PROJECT_NAME: str = "SOBERANÍA Backend"
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
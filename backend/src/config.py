import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Class for storing project-wide settings"""

    DB_USERNAME: str = (os.getenv("DB_USERNAME"))
    DB_PASSWORD: str = (os.getenv("DB_PASSWORD"))
    DB_HOST: str = (os.getenv("DB_HOST"))
    DB_NAME: str = (os.getenv("DB_NAME"))

    DATETIME_FORMAT_RESULT_PAST: str = "{d} days, {h} hours, {m} minutes and {s} seconds passed"
    DATETIME_FORMAT_RESULT_FUTURE: str = "{d} days, {h} hours, {m} minutes and {s} seconds left"

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), '.env'))


settings = Settings()

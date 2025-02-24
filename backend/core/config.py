from pydantic_settings import BaseSettings
import os

class Configs(BaseSettings):
    API: str = "/routing"

    ENV: str = os.getenv("ENV", "dev")
    DEBUG: bool = ENV == "dev"

    PROJECT_NAME: str = "verse-auth"

    PROJECT_ROOT: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    DB: str = os.getenv("DB", "postgresql")

    DB_USER: str = os.getenv("DB_USER", "admin")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "admin")  # todo

    DB_HOST: str = os.getenv("DB_HOST", "192.168.77.59")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "auth")

    DB_ENGINE: str = "postgresql+asyncpg"

    DATABASE_URI_FORMAT: str = "{db_engine}://{user}:{password}@{host}:{port}/{database}"

    DATABASE_URI: str = DATABASE_URI_FORMAT.format(
        db_engine=DB_ENGINE,
        user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT,
        database=DB_NAME,
    )

    SENTRY_KEY: str = os.getenv("SENTRY_KEY", "e81d50f3b620412681b324edb33e1423")  # todo
    SENTRY_HOST: str = os.getenv("SENTRY_HOST", "192.168.77.122")
    SENTRY_PORT: str = os.getenv("SENTRY_PORT", "9000")
    SENTRY_PRJ: str = os.getenv("SENTRY_PRJ", "13")

    SENTRY_URI_FORMAT: str = "http://{key}@{host}:{port}/{prj}"

    SENTRY_URI: str = SENTRY_URI_FORMAT.format(
        key=SENTRY_KEY,
        host=SENTRY_HOST, port=SENTRY_PORT,
        prj=SENTRY_PRJ,
    )

    class Config:
        case_sensitive: bool = True


configs = Configs()
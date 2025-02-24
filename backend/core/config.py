from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
import os

class Configs(BaseSettings):

    #Для инициализации проекта#
    PROJECT_NAME:str = "Название хакатона"
    PROJECT_DESCRIPTION:str = "Апишки для хакатона"

    #Для аутенфикации
    SECRET_KEY: str = Field(default="your-secret-key", env="SECRET_KEY")  # Секретный ключ для JWT и шифрования
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")  # Алгоритм шифрования для JWT
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")  # Время жизни токена

    # Настройки базы данных (пример для PostgreSQL)
    DATABASE_URL: Optional[str] = Field(default=None, env="DATABASE_URL")  # URL для подключения к БД
    DB_HOST: Optional[str] = Field(default="localhost", env="DB_HOST")
    DB_PORT: Optional[int] = Field(default=5432, env="DB_PORT")
    DB_USER: Optional[str] = Field(default="postgres", env="DB_USER")
    DB_NAME: Optional[str] = Field(default="mydb", env="DB_NAME")
    DB_PASS: Optional[str] = Field(default=None, env="DB_PASS")


configs = Configs()
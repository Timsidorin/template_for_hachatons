from pydantic_settings import BaseSettings
import os

class Configs(BaseSettings):

    PROJECT_NAME:str = "Название хакатона"


configs = Configs()
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL1: str 
    DATABASE_URL_SYNC: str

    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    
    # Security
    SECRET_KEY: str 
    ALGORITHM: str = "HS512"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Email
    SENDER_EMAIL: str = "alikozhabai207@gmail.com"

    SENDER_PASSWORD: str = "ljcn zfwt rjop lvgn"

    SMTP_SERVER: str = "smtp.gmail.com"

    SMTP_PORT:int  = "465"

    # OTP Settings
    OTP_EXPIRE_MINUTES: int = 5
    
    class Config:
        env_file = ".env"

settings = Settings()
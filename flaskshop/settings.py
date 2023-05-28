# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from pathlib import Path


class DBConfig:
    db_type = os.getenv("DB_TYPE", "postgresql")
    user = os.getenv("DB_USER", "admin")
    passwd = os.getenv("DB_PASSWD", "flatron")
    host = os.getenv("DB_HOST", "194.182.78.151")
    port = os.getenv("DB_PORT", 5432)
    db_name = os.getenv("DB_NAME", "db_24shop_new")
    if db_type == "postgresql":
        db_uri = f"postgresql://{user}:{passwd}@{host}:{port}/{db_name}"
    elif db_type == "mysql":
        db_uri = (
            f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db_name}?charset=utf8mb4"
        )
    redis_uri = "redis://localhost:8080"
    esearch_uri = "localhost"


class Config:
    
    #DEBUG SETTING
    ENV = "dev"
    FLASK_DEBUG = True

    SECRET_KEY = os.getenv("SECRET_KEY", "thisisashop")
    
    #REDIS SETTING
    # Redis
    # if redis is enabled, it can be used for:
    #   - cache
    #   - save product description
    #   - save page content
    USE_REDIS = False
    REDIS_URL = os.getenv("REDIS_URI", DBConfig.redis_uri)

    # Elasticsearch
    # if elasticsearch is enabled, the home page will have a search bar
    # and while add a product, the search index will get update
    USE_ES = False
    ES_HOSTS = [
        os.getenv("ESEARCH_URI", DBConfig.esearch_uri),
    ]

    # SQLALCHEMY SETTING
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", DBConfig.db_uri)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_QUERY_TIMEOUT = 0.1  # log the slow database query, and unit is second
    SQLALCHEMY_RECORD_QUERIES = True

    # DIR SETTING
    APP_DIR = Path(__file__).parent  # This directory
    PROJECT_ROOT = APP_DIR.parent
    STATIC_DIR = APP_DIR / "static"
    UPLOAD_FOLDER = "upload"
    UPLOAD_DIR = STATIC_DIR / UPLOAD_FOLDER
    DASHBOARD_TEMPLATE_FOLDER = APP_DIR / "templates" / "dashboard"
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "static/placeholders")

    PURCHASE_URI = os.getenv("PURCHASE_URI", "")

    BCRYPT_LOG_ROUNDS = 13
    DEBUG_TB_ENABLED = os.getenv("FLASK_DEBUG", False)  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = True

    MESSAGE_QUOTA = 10
    
    # LANGUAGES SETTING
    LANGUAGES = {"en": "English", "bg": "Български"}
    BABEL_DEFAULT_LOCALE = os.getenv("BABEL_DEFAULT_LOCALE", "en_US")
    BABEL_DEFAULT_TIMEZONE = os.getenv("BABEL_DEFAULT_TIMEZONE", "UTC")
    BABEL_TRANSLATION_DIRECTORIES = os.getenv(
        "BABEL_TRANSLATION_DIRECTORIES", "../translations"
    )
    BABEL_CURRENCY = os.getenv("BABEL_CURRENCY", "EUR")
    
    # MAIL SETTING
    MAIL_SERVER = os.getenv("MAIL_SERVER", "imap.gmail.com")
    MAIL_PORT = os.getenv("MAIL_PORT", 587)
    MAIL_TLS = os.getenv("MAIL_TLS", False)
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "volodymyr.dehtiarenko@gmail.com")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "_Green1975_")

    GA_MEASUREMENT_ID = os.getenv("GA_MEASUREMENT_ID", "")


    # MIGRATION
    TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsInN1YiI6OTc2MzU2LCJpYXQiOjE2NzcxODM5MDZ9.CZk2L11F2LdqSO5Ww8ALKJjJcINQWpVN4t9Q4EjY-NA'
    URL_PRODUCTS =   'https://www.btswholesaler.com/generatefeedbts'
    URL_CATEGORIES = 'https://www.btswholesaler.com/generatefeedcategoriesbts'
    USER_ID = '52807223'
    USER_PASS = 'flatron1975'
    FORMAT_FEED = 'csv'

class ProdConfig(Config):
    ENV = "prod"
    FLASK_DEBUG = False
    DEBUG_TB_ENABLED = False

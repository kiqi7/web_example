class Config:
    # Secret key for Flask session management and CSRF protection
    SECRET_KEY = 'your_secret_key_here'

    # Database connection string for MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@hostname:port/database_name'

    # Additional configuration for SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other Flask configurations
    DEBUG = True  # Set to False in production

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'production_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@hostname:port/database_name'

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'development_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@hostname:port/database_name'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # Using SQLite for testing

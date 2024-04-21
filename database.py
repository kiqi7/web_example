from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
import os

user = 'chat_user'
password = '12345678'
host = 'localhost'  # This could be 'localhost' if using the Cloud SQL Proxy
dbname = 'ChatHistoryDB'
instance_connection_name = 'myproject-20230413:us-central1:chat' # For Cloud SQL Proxy

DATABASE_URL = f"mysql+aiomysql://{user}:{password}@{host}/{dbname}?unix_socket=/cloudsql/{instance_connection_name}&charset=utf8mb4"


# DATABASE_URL = "mysql+aiomysql://<user>:<password>@<host>/<dbname>"  # Update this line with your actual credentials
# DATABASE_URL = "mysql+aiomysql://<user>:<password>@<public_ip>/<dbname>?charset=utf8mb4"
# DATABASE_URL = "mysql+aiomysql://<user>:<password>@localhost/<dbname>?unix_socket=/cloudsql/myproject-20230413:us-central1:chat&charset=utf8mb4"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # No change in usage, just updated the import
database = Database(DATABASE_URL)

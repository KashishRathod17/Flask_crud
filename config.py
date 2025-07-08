import os
from dotenv import load_dotenv

load_dotenv()

class Config:       
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_SERVER = os.getenv("DB_SERVER","localhost")
    DB_DATABASE = os.getenv("DB_DATABASE")

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS =  True
    SQLALCHEMY_ECHO = True
    
    # 'mysql+pymysql://root:pass1234@localhost/dbname'
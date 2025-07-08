class Config:       
    DB_USER = 'root'
    DB_PASSWORD = 'kashish1234'
    DB_SERVER = 'localhost'
    DB_DATABASE = 'flaskapp'

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS =  True
    SQLALCHEMY_ECHO = True
    
    # 'mysql+pymysql://root:pass1234@localhost/dbname'
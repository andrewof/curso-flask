from decouple import config

class Config:
    DEBUG = True
    SECRET_KEY = 'wel#come#1102'
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_DB = "tienda"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 # TLS: Transport Layer Security (seguridad de la capa de transporte)
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'luisgonzalo187@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    

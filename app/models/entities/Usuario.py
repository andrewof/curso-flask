from flask_login import UserMixin
import bcrypt

class Usuario(UserMixin):
    
    def __init__(self, id, usuario, password, tipousuario):
        self.id = id 
        self.usuario = usuario
        self.password = password
        self.tipousuario = tipousuario
    
    @classmethod
    def verificar_password(self, password, encriptado):
        return bcrypt.checkpw(password, encriptado)
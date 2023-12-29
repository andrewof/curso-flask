from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario

class ModeloUsuario():
    
    @classmethod
    def login(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, usuario, password 
                    FROM usuario WHERE usuario = '{0}'""".format(usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                coincide = Usuario.verificar_password(usuario.password.encode('utf-8'), data[2].encode('utf-8'))
                if coincide:
                    usuario_logeado = Usuario(data[0], data[1], None, None)
                    return usuario_logeado
                else:
                    return None
            else:
                return None
        except Exception as ex:
            print(ex)
            raise ex
    
    @classmethod      
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT USU.id, USU.usuario, TIP.id, TIP.nombre 
                    FROM usuario USU JOIN tipousuario TIP ON USU.tipousuario_id = TIP.id WHERE USU.id = {0}""".format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            tipousuario = TipoUsuario(data[2], data[3]) # data[2] = id, data[3] = nombre
            usuario_logeado = Usuario(data[0], data[1], None, tipousuario)
            return usuario_logeado
        except Exception as ex:
            print(ex)
            raise ex
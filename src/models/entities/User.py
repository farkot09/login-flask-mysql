from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):
    @classmethod
    def __init__(self, id_usuario, nombre, apellido, email, password):
        self.id_usuario = id_usuario        
        self.nombre = nombre 
        self.apellido = apellido
        self.email = email
        self.password = password
      
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    def get_id(self):
        return str(self.id_usuario)


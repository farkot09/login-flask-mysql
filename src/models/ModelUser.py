from .entities.User import User

class ModelUser():

    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id_usuario, nombre, apellido, email, password 
            FROM usuarios 
            WHERE email='{}' """.format(user.email)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],row[2],row[3], User.check_password(row[4], user.password))
                return user
            else:
                return None

            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id_usuario, nombre, apellido, email 
            FROM usuarios 
            WHERE id_usuario='{}' """.format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                return User(row[0],row[1],row[2],row[3], None)
                
            else:
                return None

            
        except Exception as ex:
            raise Exception(ex)
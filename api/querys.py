from api.conexion import *

class querys:

    def __init__(self):
        self.conexion_ = conexion()

    def get_user_by_username_and_password(self, username, password):

        query = 'SELECT * FROM `usuarios` WHERE `usuarios`.`nombre_usuario` = "' + username + '" AND contrasena="' + password + '"'

        cursor = self.conexion_.conector.cursor() 
        cursor.execute(query)
        return cursor.fetchone()

    def insert_(self, data):

        cursor = self.conexion_.conector.cursor()

        insql = "INSERT INTO `motos` (`precio`, `marca`, `modelo`, `ano`, `color`, `kilometraje`) VALUES (%s, %s, %s, %s, %s, %s)"
        
        datos = (float(data['precio']), data['marca'], data['modelo'], int(data['anio']),
                 data['color'], data['kilometraje'])
        cursor.execute(insql, datos)
        self.conexion_.conector.commit()

    def get_all(self):
        
        query = 'SELECT * FROM `motos` ORDER BY `ID` DESC limit 100'

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def delete(self, id):
        query = 'DELETE FROM `motos` WHERE `id` = %s'

        datos = (id,)

        cursor = self.conexion_.conector.cursor()
        cursor.execute(query, datos)
        self.conexion_.conector.commit()

    def update_record(self, data, id):

        update_sql = """   UPDATE `motos` SET 
        `precio`= %s,
        `marca`=%s,        `modelo`=%s,
        `ano`=%s,`color`=%s,
        `kilometraje`=%s
        WHERE  `id` = %s """

        datos = (float(data['precio']), data['marca'], data['modelo'], int(data['anio']),
                 data['color'], data['kilometraje'], id)

        cursor = self.conexion_.conector.cursor()
        cursor.execute(update_sql, datos)
        self.conexion_.conector.commit()


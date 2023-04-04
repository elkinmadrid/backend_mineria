import mysql.connector
import os

class conexion:

    conector = None

    def __init__(self):

        direccion_servidor = os.environ['HOST']
        nombre_bd = os.environ['NAME_BD']
        nombre_usuario = os.environ['USERNAME']
        password = os.environ['PASSWORD']
        try:
            self.conector = mysql.connector.connect(host=direccion_servidor,
                                                     user=nombre_usuario,
                                                     password=password,
                                                     database=nombre_bd)


            print("ok")
            #return self.conector

            # OK! conexión exitosa
        except Exception as e:
            # Atrapar error
            print("Ocurrió un error al conectar a MySql: ", e)
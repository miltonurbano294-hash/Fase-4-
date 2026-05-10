from datetime import datetime


def registrar_log(mensaje):

    archivo = open("logs.txt", "a")

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    archivo.write("[{0}] {1}\n".format(fecha, mensaje))

    archivo.close()
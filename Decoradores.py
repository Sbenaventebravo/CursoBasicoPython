#Decoradores (pueden ser funciones o clases)
# puede servir para sobrecargar clases y metodos

def decorador_usuario_existe(nombre_funcion):
    def funcion_decorada(argumento):
        try:
            verificar_usuario(argumento) #consulta a la base de datos
        except:
            print("Usuario no existe")
        else:
            nombre_funcion(argumento) # funcion decorada
    return funcion_decorada()

@decorador_usuario_existe
def mi_reporte_de_sesiones(id_usuario):
    pass # bloque del codigo a ejecutar
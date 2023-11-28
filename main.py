from os import system
from modelo_orm import *
from gestionar_obra import *

#MENU:
#Vamos a crear una clase menu porque creemos que la complejidad del menu puede seguir aumentando de acuerdo a las mejoras que deseemos implementar
class Menu:
    def __init__(self, title,options):
        self.title = title
        self.options = options
    #se encarga de mostrar el menú y manejar la interacción del user
    def menu_display(self):
        #iniciamos un bucle infinito hasta que el user envie como dato de entrada un '0':exit
        while True:
            #El metodo clear_screen funciona para limpiar el menu
            
            #salida: "Obras Urbanas Ciudad IFTS 18"
            print(self.title)
            
            
            #salida: opciones del menu...
            for key, value in self.options.items():
                if callable(value):  # Verifica si el valor es una función
                    print(f"{key}. {value.__doc__ or value.__name__}")  # Usa el docstring o el nombre de la función
                else:
                    print(f"{key}. {value}")
                
            #var donde guardo la opcion elegida por el user
            mi_opcion = input("Selecciona una opción: \n (recuerda utilizar el numero indicado)")
            #matcheo 
            if mi_opcion == '0': #rompe el bucle y sale del menú.
                break
            elif mi_opcion in self.options: #ejecuta la función asociada a esa opción.
                self.options[mi_opcion]()
            else:
                input("Opción no válida. Presiona Enter para continuar.") 
    
    
        
def crear_nueva_obra():
    GestionarObra.nueva_obra()
def obtener_indicadores():
   GestionarObra.obtener_indicadores()
   
def exit():
    print("Cerrando el sistema. Hasta luego")
    sqlite_db.close()
    
# Opciones del menú principal
menu_options = {
    '1': crear_nueva_obra,
    '2': obtener_indicadores,
    #'3': finalizar_obra,
    #'4': rescindir_obra,
    '0': exit
}

if __name__ == "__main__":
    
    GestionarObra.extraer_datos()
    GestionarObra.conectar_db()
    GestionarObra.mapear_orm()
    GestionarObra.limpiar_datos()
    print(GestionarObra.cargar_datos()) 
        # Llamar al método de clase para obtener e imprimir los indicadores
        #~comentario nuevo
    
    
    main_menu = Menu("Obras Urbanas Ciudad IFTS 18", menu_options)
    main_menu.menu_display()

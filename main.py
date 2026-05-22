# Importación de funciones según la regla del TP (from modulo import funcion)
from operaciones import registrar_usuario, depositar, extraer
from historial import mostrar_historial, guardar_historial, cargar_historial

def main():
    # Tarea 2: Inicializar la variable saldo
    saldo = 0.0
    
    # Tarea 3: Inicializar la lista vacía para el historial
    historial = []
    
    print("¡Bienvenido a la Billetera Digital UAI!")
    
    # Opcional pero recomendado según las reglas generales (Funcionalidad 1)
    # Llamamos a la función de registro antes de entrar al menú
    usuario = registrar_usuario()
    print(f"\nUsuario {usuario} registrado con éxito. Ingresando al sistema...\n")

    # Tarea 4: Bucle while True para el menú interactivo
    while True:
        print("\n" + "="*30)
        print(" Menú Principal - Billetera UAI")
        print("="*30)
        print("1. Depositar dinero")
        print("2. Extraer dinero")
        print("3. Ver historial")
        print("4. Guardar historial en archivo")
        print("5. Cargar historial desde archivo")
        print("6. Salir")
        print("="*30)

        # Tarea 5: Solicitar opción
        opcion = input("Seleccione una opción: ")

        # Tarea 6 y 7: Controlar la opción y llamar a las funciones correspondientes
        if opcion == "1":
            # Pasamos saldo e historial y recibimos los valores actualizados
            saldo, historial = depositar(saldo, historial)
            
        elif opcion == "2":
            # Lo mismo para extraer
            saldo, historial = extraer(saldo, historial)
            
        elif opcion == "3":
            mostrar_historial(historial)
            
        elif opcion == "4":
            guardar_historial(historial)
            
        elif opcion == "5":
            historial = cargar_historial(historial)
            
        elif opcion == "6":
            print("\nSaliendo del programa. ¡Gracias por usar la Billetera Digital UAI!")
            # Tarea 8: Finalizar con break
            break
            
        else:
            print("\n❌ Opción no válida. Por favor, ingrese un número del 1 al 6.")

# Este bloque asegura que el programa se ejecute solo si se abre directamente este archivo
if __name__ == "__main__":
    main()
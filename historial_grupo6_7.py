
def guardar_historial(historial):
    try:
        archivo = open("datos.txt", "w")
        
        for movimiento in historial:
            archivo.write(f"{movimiento['tipo']};{movimiento['monto']}\n")
        
        archivo.close()
        print("Historial guardado correctamente.")
    
    except:
        print("Error al guardar el historial.")



def cargar_historial():
    try:
        archivo = open("datos.txt", "r")
        
        lineas = archivo.readlines()
        archivo.close()

        historial = []

        for linea in lineas:
            datos = linea.strip().split(";")

            movimiento = {
                "tipo": datos[0],
                "monto": float(datos[1])
            }

            historial.append(movimiento)

        return historial

    except FileNotFoundError:
        print("No existe un historial guardado previamente.")
        return []

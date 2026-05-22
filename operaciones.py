def registrar_usuario():
    nombre = input("Ingrese su nombre: ").strip().title()
    correo = input("Ingrese su correo electrónico: ").strip()
    datos_usuario = {
        "nombre": nombre,
        "correo": correo
    }
    usuario = []
    usuario.append(datos_usuario)

    return datos_usuario


def deposite(balance, history):
    COMPARATION = 0 
    try:
        amount = float(input("Ingrese el monto a depositar: "))
        if amount <= float(COMPARATION):
            print("Error: el monto debe ser mayor que cero.")
            raise ValueError("El monto debe ser mayor que cero.")
        else: 
            balance += amount
            movement = {
                "type": "Depósito",
                "amount": amount,
            }
            history = []
            history.append(movement)
            print(f"Depósito exitoso. Nuevo balance: {balance:.2f}")
            return balance, history
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return balance, history


def extraer(saldo, historial):
    try:
        monto = float(input("Ingrese el monto a extraer: "))
    except ValueError:
        print("Error: debe ingresar un número válido.")
        return saldo, historial

    if monto > 0 and monto <= saldo:
        saldo = saldo - monto
        
        movimiento = {
            "tipo": "Extracción",
            "monto": monto
        }
        
        historial.append(movimiento)
        
        print("Extracción exitosa. Retiró: ${monto}")
        return saldo, historial
    else:
        print("Operación inválida o saldo insuficiente.")
        return saldo, historial

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

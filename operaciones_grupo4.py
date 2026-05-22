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

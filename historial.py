def mostrar_historial(historial, saldo=0):
    if len(historial) == 0:
        print("No hay movimientos registrados.")
    else:
        for movimiento in historial:
            print(movimiento["type"])
            print(movimiento["amount"])
    print(f"Saldo actual: ${saldo:.2f}")
   
def mostrar_historial(historial, saldo):
    if len(historial) == 0:
        print("No hay movimientos registrados.")
    else:
        for movimiento in historial:
            print(movimiento["tipo"])
            print(movimiento["monto"])
    print(f"Saldo actual: ${saldo:.2f}")
   
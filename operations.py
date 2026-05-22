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

deposite(1000, [])
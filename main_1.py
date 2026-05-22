from operaciones import registrar_usuario


usuario = registrar_usuario()
print(f"Usuario registrado: {usuario['nombre']}, {usuario['correo']}")
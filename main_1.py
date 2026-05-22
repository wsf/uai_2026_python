from operaciones import registrar_usuario
from historial import mostrar_historial

usuario = registrar_usuario()
print(f"Usuario registrado: {usuario['nombre']}, {usuario['correo']}")
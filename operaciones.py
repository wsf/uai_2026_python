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



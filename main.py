import os
import hashlib

def clear():
    """
    Limpia la consola, considerando diferentes sistemas operativos.
    En Windows usa 'cls', en Unix/Linux/Mac usa 'clear'.
    """
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/Mac
        os.system('clear')

def input_con_control(mensaje):
    """
    Maneja las entradas de usuario con control de errores.

    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario para solicitar entrada.

    Retorna:
    str: La entrada del usuario.
    """
    try:
        return input(mensaje)
    except (KeyboardInterrupt, EOFError):
        print("\nEntrada cancelada.")
        return ""

def hash_password(password):
    """
    Hashea una contraseña utilizando SHA-256.

    Parámetros:
    password (str): La contraseña a hashear.

    Retorna:
    str: La contraseña hasheada.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def mostrar_mensaje_y_pausar(mensaje):
    """
    Muestra un mensaje al usuario y pausa la pantalla hasta que el usuario presione Enter.

    Parámetros:
    mensaje (str): El mensaje a mostrar.
    """
    print(mensaje)
    input("\nPresiona Enter para continuar...")

def validar_longitud(valor, min_longitud, max_longitud):
    """
    Valida la longitud de una cadena.

    Parámetros:
    valor (str): La cadena a validar.
    min_longitud (int): La longitud mínima permitida.
    max_longitud (int): La longitud máxima permitida.

    Retorna:
    str o None: Un mensaje de error si la longitud no es válida, de lo contrario None.
    """
    if len(valor) < min_longitud:
        return f"Debe tener al menos {min_longitud} caracteres."
    elif len(valor) > max_longitud:
        return f"Debe tener como máximo {max_longitud} caracteres."
    return None

def solicitar_entrada(mensaje, min_longitud, max_longitud):
    """
    Solicita una entrada al usuario con validación de longitud.

    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario para solicitar entrada.
    min_longitud (int): La longitud mínima permitida.
    max_longitud (int): La longitud máxima permitida.

    Retorna:
    str: La entrada del usuario validada.
    """
    while True:
        valor = input_con_control(mensaje)
        error = validar_longitud(valor, min_longitud, max_longitud)
        if error:
            mostrar_mensaje_y_pausar(error)
        else:
            return valor

def verificar_usuario_existe(usuario):
    """
    Verifica si el nombre de usuario ya está registrado.

    Parámetros:
    usuario (str): El nombre de usuario a verificar.

    Retorna:
    bool: True si el usuario existe, False en caso contrario.
    """
    for dict_usuario in usuarios_registrados:
        if usuario == dict_usuario["usuario"]:
            return True
    return False

def mostrar_requisitos():
    """
    Muestra los requisitos para el nombre de usuario y la contraseña.
    """
    requisitos_usuario = (
        "Requisitos para el nombre de usuario:\n"
        "- Longitud: 3 a 20 caracteres\n"
        "- Puede incluir letras y números\n"
        "- Evitar caracteres especiales y espacios en blanco"
    )
    requisitos_password = (
        "Requisitos para la contraseña:\n"
        "- Longitud: 8 a 20 caracteres\n"
        "- Debe incluir letras (mayúsculas y minúsculas), números y caracteres especiales\n"
        "- No debe contener el nombre de usuario"
    )
    mostrar_mensaje_y_pausar(f"{requisitos_usuario}\n\n{requisitos_password}")

def iniciar_sesion():
    """
    Permite al usuario iniciar sesión en el sistema.

    Retorna:
    bool: True si el inicio de sesión es exitoso, False en caso contrario.
    """
    print("\n### INICIAR SESIÓN ###\n")
    usuario = solicitar_entrada("Usuario: ", 3, 20)
    password = solicitar_entrada("Contraseña: ", 8, 20)

    if not usuario or not password:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña no pueden estar vacíos.")
        return False

    password_hashed = hash_password(password)

    if usuario == "teo" and password_hashed == hash_password("123"):
        mostrar_mensaje_y_pausar("\n¡Has iniciado sesión con éxito!")
        return True

    for dict_usuario in usuarios_registrados:
        if usuario == dict_usuario["usuario"] and password_hashed == dict_usuario["password"]:
            mostrar_mensaje_y_pausar("\n¡Has iniciado sesión con éxito!")
            return True

    mostrar_mensaje_y_pausar("\nUsuario o contraseña incorrectos.")
    return False

def registrar_usuario():
    """
    Permite al usuario registrarse en el sistema.

    Muestra los requisitos para el nombre de usuario y la contraseña, y valida si el nombre de usuario ya está registrado.
    """
    print("\n### REGISTRARSE ###")
    mostrar_requisitos()
    usuario = solicitar_entrada("Usuario: ", 3, 20)

    if verificar_usuario_existe(usuario):
        mostrar_mensaje_y_pausar("\nEl nombre de usuario ya está registrado. Intenta con otro.")
        return

    password = solicitar_entrada("Contraseña: ", 8, 20)


    password_hashed = hash_password(password)
    dict_usuario = {"usuario": usuario, "password": password_hashed}
    usuarios_registrados.append(dict_usuario)
    mostrar_mensaje_y_pausar("\nTe has registrado exitosamente.")

def personalizar_perfil():
    """
    Permite al usuario personalizar su perfil, cambiando el nombre de usuario y la contraseña.

    Verifica la validez del usuario actual antes de realizar cambios.
    """
    print("\n### PERSONALIZAR PERFIL ###\n")
    usuario_actual = solicitar_entrada("Usuario actual: ", 3, 20)
    password_actual = solicitar_entrada("Contraseña actual: ", 8, 20)

    if not usuario_actual or not password_actual:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña no pueden estar vacíos.")
        return

    password_hashed = hash_password(password_actual)
    usuario_valido = False

    for dict_usuario in usuarios_registrados:
        if usuario_actual == dict_usuario["usuario"] and password_hashed == dict_usuario["password"]:
            usuario_valido = True
            break

    if not usuario_valido:
        mostrar_mensaje_y_pausar("\nUsuario o contraseña incorrectos.")
        return

    nuevo_usuario = solicitar_entrada("Nuevo usuario: ", 3, 20)

    if verificar_usuario_existe(nuevo_usuario):
        mostrar_mensaje_y_pausar("\nEl nuevo nombre de usuario ya está registrado. Intenta con otro.")
        return

    nuevo_password = solicitar_entrada("Nueva contraseña: ", 8, 20)
    nuevo_password_hashed = hash_password(nuevo_password)
    for dict_usuario in usuarios_registrados:
        if usuario_actual == dict_usuario["usuario"]:
            dict_usuario["usuario"] = nuevo_usuario
            dict_usuario["password"] = nuevo_password_hashed
            break

    mostrar_mensaje_y_pausar("\nPerfil actualizado exitosamente.")

def confirmar_salida():
    """
    Solicita confirmación al usuario antes de salir del programa.

    Retorna:
    bool: True si el usuario confirma que desea salir, False en caso contrario.
    """
    while True:
        confirmacion = input_con_control("¿Estás seguro que deseas salir? (s/n): ").lower()
        if confirmacion in ['s', 'n']:
            return confirmacion == 's'
        else:
            mostrar_mensaje_y_pausar("Respuesta inválida. Por favor, ingresa 's' para sí o 'n' para no.")

def imprimir_menu_principal():
    """
    Imprime el menú principal después de iniciar sesión.
    """
    print("\n### MENÚ PRINCIPAL ###\n")
    print("1) Personalizar perfil")
    print("2) Cerrar sesión")
    print("3) Salir")

# Lista de usuarios registrados
usuarios_registrados = []

# Usuario predeterminado
usuarios_registrados.append({"usuario": "teo", "password": hash_password("12345678")})

# Verificar si el usuario ha iniciado sesión
sesion_iniciada = False

# Menú principal
while True:
    try:
        clear()
        print("\n#### BIENVENIDO AL SISTEMA ####\n")
        print("1) Iniciar sesión")
        print("2) Registrarse")
        print("3) Salir")
        opcion = input_con_control("\nSelecciona una opción: ")

        if opcion == "1":
            if iniciar_sesion():
                sesion_iniciada = True
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            if confirmar_salida():
                break
        else:
            mostrar_mensaje_y_pausar("\nOpción inválida. Por favor, selecciona una opción válida.")
        
        while sesion_iniciada:
            clear()
            imprimir_menu_principal()
            opcion_menu = input_con_control("\nSelecciona una opción: ")
            if opcion_menu == "1":
                personalizar_perfil()
            elif opcion_menu == "2":
                mostrar_mensaje_y_pausar("\n¡Has cerrado sesión!")
                sesion_iniciada = False
            elif opcion_menu == "3":
                if confirmar_salida():
                    sesion_iniciada = False
                    break
            else:
                mostrar_mensaje_y_pausar("\nOpción inválida. Por favor, selecciona una opción válida.")

    except Exception as e:
        print(f"Ocurrió un error durante la ejecución del programa: {e}")
        mostrar_mensaje_y_pausar("Se produjo un error inesperado. El programa se cerrará.")

print("\n¡Hasta luego!\n")

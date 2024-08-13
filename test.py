import os
import hashlib

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def input_con_control(mensaje):
    try: return input(mensaje)
    except (KeyboardInterrupt, EOFError): return ""

def hash_password(password): return hashlib.sha256(password.encode()).hexdigest()

def mostrar_mensaje_y_pausar(mensaje): input(f"{mensaje}\nPresiona Enter para continuar...")

def solicitar_entrada(mensaje, min_longitud, max_longitud):
    while True:
        valor = input_con_control(mensaje)
        if len(valor) < min_longitud or len(valor) > max_longitud:
            mostrar_mensaje_y_pausar(f"Debe tener entre {min_longitud} y {max_longitud} caracteres.")
        else: return valor

def verificar_usuario_existe(usuario):
    return any(usuario == u["usuario"] for u in usuarios_registrados)

def iniciar_sesion():
    print("\n### INICIAR SESIÓN ###")
    usuario, password = solicitar_entrada("Usuario: ", 3, 20), solicitar_entrada("Contraseña: ", 8, 20)
    if any(usuario == u["usuario"] and hash_password(password) == u["password"] for u in usuarios_registrados):
        mostrar_mensaje_y_pausar("¡Has iniciado sesión con éxito!")
        return True
    mostrar_mensaje_y_pausar("Usuario o contraseña incorrectos.")
    return False

def registrar_usuario():
    print("\n### REGISTRARSE ###")
    usuario = solicitar_entrada("Usuario: ", 3, 20)
    if verificar_usuario_existe(usuario):
        mostrar_mensaje_y_pausar("El nombre de usuario ya está registrado.")
        return
    password = solicitar_entrada("Contraseña: ", 8, 20)
    usuarios_registrados.append({"usuario": usuario, "password": hash_password(password)})
    mostrar_mensaje_y_pausar("Te has registrado exitosamente.")

def personalizar_perfil():
    print("\n### PERSONALIZAR PERFIL ###")
    usuario_actual, password_actual = solicitar_entrada("Usuario actual: ", 3, 20), solicitar_entrada("Contraseña actual: ", 8, 20)
    for u in usuarios_registrados:
        if u["usuario"] == usuario_actual and u["password"] == hash_password(password_actual):
            nuevo_usuario = solicitar_entrada("Nuevo usuario: ", 3, 20)
            if verificar_usuario_existe(nuevo_usuario):
                mostrar_mensaje_y_pausar("El nuevo nombre de usuario ya está registrado.")
                return
            u["usuario"], u["password"] = nuevo_usuario, hash_password(solicitar_entrada("Nueva contraseña: ", 8, 20))
            mostrar_mensaje_y_pausar("Perfil actualizado exitosamente.")
            return
    mostrar_mensaje_y_pausar("Usuario o contraseña incorrectos.")

def confirmar_salida():
    while True:
        confirmacion = input_con_control("¿Estás seguro que deseas salir? (s/n): ").lower()
        if confirmacion in ['s', 'n']: return confirmacion == 's'

def imprimir_menu_principal():
    print("\n### MENÚ PRINCIPAL ###\n1) Personalizar perfil\n2) Cerrar sesión\n3) Salir")

usuarios_registrados, sesion_iniciada = [{"usuario": "teo", "password": hash_password("12345678")}], False

while True:
    clear()
    print("\n#### BIENVENIDO AL SISTEMA ####\n1) Iniciar sesión\n2) Registrarse\n3) Salir")
    opcion = input_con_control("\nSelecciona una opción: ")
    if opcion == "1" and iniciar_sesion(): sesion_iniciada = True
    elif opcion == "2": registrar_usuario()
    elif opcion == "3" and confirmar_salida(): break
    
    while sesion_iniciada:
        clear()
        imprimir_menu_principal()
        opcion_menu = input_con_control("\nSelecciona una opción: ")
        if opcion_menu == "1": personalizar_perfil()
        elif opcion_menu == "2": mostrar_mensaje_y_pausar("¡Has cerrado sesión!"); sesion_iniciada = False
        elif opcion_menu == "3" and confirmar_salida(): sesion_iniciada = False; break

print("\n¡Hasta luego!\n")

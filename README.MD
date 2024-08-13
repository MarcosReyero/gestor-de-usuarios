# Sistema de Gestión de Usuarios

Este proyecto es una aplicación de gestión de usuarios desarrollada en Python. Su objetivo es llevar más allá la consigna de la primera pre-entrega del curso, añadiendo funcionalidades adicionales y mejorando el control de errores y la interacción con el usuario.

## Objetivo

El objetivo de esta aplicación es permitir a los usuarios iniciar sesión, registrarse, y personalizar su perfil, todo mientras se garantiza una experiencia de usuario fluida y segura. El sistema incluye funcionalidades para la validación de entradas y manejo de errores, así como una estructura que soporta múltiples usuarios con contraseñas seguras.

## Funcionamiento General

### 1. `clear()`

Limpia la consola de comandos, adaptándose a diferentes sistemas operativos:
- **Windows**: usa el comando `cls`.
- **Unix/Linux/Mac**: usa el comando `clear`.

### 2. `input_con_control(mensaje)`

Solicita entrada al usuario y maneja posibles errores de entrada (como interrupciones por teclado o errores de fin de archivo). Si ocurre un error, informa al usuario y devuelve una cadena vacía.

### 3. `hash_password(password)`

Hashea una contraseña utilizando el algoritmo SHA-256. Este método se utiliza para almacenar contraseñas de forma segura en lugar de guardar texto plano.

### 4. `mostrar_mensaje_y_pausar(mensaje)`

Muestra un mensaje al usuario y pausa la ejecución del programa hasta que el usuario presione Enter. Esto se usa para proporcionar retroalimentación al usuario y permitirle leer mensajes importantes.

### 5. `validar_longitud(valor, min_longitud, max_longitud)`

Valida que una cadena de texto esté dentro de un rango específico de longitud. Retorna un mensaje de error si la longitud no es válida, o `None` si es válida.

### 6. `solicitar_entrada(mensaje, min_longitud, max_longitud)`

Solicita una entrada al usuario con un mensaje específico y valida que la longitud de la entrada esté dentro de los límites establecidos. Repite la solicitud hasta que la entrada sea válida.

### 7. `verificar_usuario_existe(usuario)`

Verifica si un nombre de usuario ya está registrado en la lista de usuarios. Retorna `True` si el usuario existe y `False` si no.

### 8. `mostrar_requisitos()`

Muestra los requisitos para el nombre de usuario y la contraseña. Proporciona pautas sobre la longitud y los caracteres permitidos.

### 9. `iniciar_sesion()`

Permite a un usuario iniciar sesión en el sistema. Solicita el nombre de usuario y la contraseña, los valida y muestra un mensaje de éxito o error basado en la validez de las credenciales.

### 10. `registrar_usuario()`

Permite a un nuevo usuario registrarse en el sistema. Muestra los requisitos para el nombre de usuario y la contraseña, verifica que el nombre de usuario no esté ya registrado, y almacena las credenciales de forma segura.

### 11. `personalizar_perfil()`

Permite a un usuario que ha iniciado sesión cambiar su nombre de usuario y contraseña. Verifica las credenciales actuales del usuario antes de permitir cambios y asegura que el nuevo nombre de usuario no esté ya registrado.

### 12. `confirmar_salida()`

Solicita confirmación al usuario antes de salir del programa. Permite al usuario cancelar la salida si decide que no desea cerrar el programa.

### 13. `imprimir_menu_principal()`

Imprime el menú principal después de que el usuario ha iniciado sesión. Permite al usuario personalizar su perfil, cerrar sesión o salir del programa.

## Uso

1. **Inicialización**: Ejecuta el script en una terminal para comenzar.
2. **Interacción**: Sigue las instrucciones en pantalla para iniciar sesión, registrarte, o personalizar tu perfil.
3. **Manejo de Errores**: El programa maneja errores de entrada y proporciona retroalimentación clara en caso de errores o acciones inválidas.

## Requisitos

- Python 3.x

## Instalación

No es necesario instalar dependencias adicionales para este proyecto. Simplemente clona el repositorio y ejecuta el archivo `main.py`

```bash
git clone https://github.com/tu-usuario/mi-proyecto.git
cd mi-proyecto
python main.py

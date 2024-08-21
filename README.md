Descripción

Crear una aplicación de consola que permita al usuario crear, leer, actualizar y eliminar notas. Las notas se almacenarán en un archivo de texto, y la interfaz será completamente basada en texto.
Requisitos

    Interacción en consola: La aplicación funcionará en la línea de comandos.
    Gestión de archivos: Las notas se almacenarán en un archivo de texto.
    Manipulación de datos: Uso de listas y diccionarios para gestionar las notas.
    
Explicación del Código

    Carga y Guardado de Notas:
        load_notes() lee las notas del archivo notes.txt. Si el archivo no existe, devuelve una lista vacía.
        save_notes() guarda la lista de notas en el archivo notes.txt.

    Interfaz de Usuario:
        display_menu() muestra el menú principal y devuelve la opción seleccionada por el usuario.
        create_note(), view_notes(), update_note(), y delete_note() manejan las operaciones de notas correspondientes.

    Gestión de Notas:
        Las notas se almacenan en una lista y se guardan en un archivo de texto para persistencia.

import os

NOTES_FILE = 'notes.txt'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            notes = file.readlines()
        return [note.strip() for note in notes]
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w') as file:
        for note in notes:
            file.write(note + '\n')

def display_menu():
    print("\nSistema de Gestión de Notas")
    print("1. Crear Nota")
    print("2. Ver Notas")
    print("3. Actualizar Nota")
    print("4. Eliminar Nota")
    print("5. Salir")
    choice = input("Elige una opción: ")
    return choice

def create_note(notes):
    note = input("Introduce el contenido de la nota: ")
    notes.append(note)
    save_notes(notes)
    print("Nota creada exitosamente.")

def view_notes(notes):
    if not notes:
        print("No hay notas para mostrar.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def update_note(notes):
    view_notes(notes)
    try:
        index = int(input("Introduce el número de la nota a actualizar: ")) - 1
        if 0 <= index < len(notes):
            new_content = input("Introduce el nuevo contenido de la nota: ")
            notes[index] = new_content
            save_notes(notes)
            print("Nota actualizada exitosamente.")
        else:
            print("Número de nota inválido.")
    except ValueError:
        print("Entrada inválida. Introduce un número.")

def delete_note(notes):
    view_notes(notes)
    try:
        index = int(input("Introduce el número de la nota a eliminar: ")) - 1
        if 0 <= index < len(notes):
            notes.pop(index)
            save_notes(notes)
            print("Nota eliminada exitosamente.")
        else:
            print("Número de nota inválido.")
    except ValueError:
        print("Entrada inválida. Introduce un número.")

def main():
    notes = load_notes()
    while True:
        choice = display_menu()
        if choice == '1':
            create_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            update_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

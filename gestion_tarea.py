import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")

# Campo de entrada para añadir nuevas tareas
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Crear un Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Función para añadir una nueva tarea
def add_task(event=None):
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Función para marcar la tarea seleccionada como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task = task_listbox.get(selected_task_index)
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, f"{task} (Completada)")
    except:
        messagebox.showwarning("Selección inválida", "Por favor, seleccione una tarea para completar.")

# Función para eliminar la tarea seleccionada
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()
        if selected_task_index:
            task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selección inválida", "Por favor, seleccione una tarea para eliminar.")

# Función para cerrar la aplicación
def close_application(event=None):
    root.quit()

# Crear botones para añadir tarea, completar tarea y eliminar tarea
add_button = tk.Button(root, text="Añadir tarea", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Marcar como completada", command=mark_completed)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar tarea", command=delete_task)
delete_button.pack(pady=5)

# Asociar atajos de teclado con las funciones
root.bind("<Return>", add_task)  # Atajo de teclado para añadir tarea (Enter)
root.bind("<c>", lambda event=None: mark_completed())  # Atajo de teclado para marcar como completada (C)
root.bind("<d>", lambda event=None: delete_task())  # Atajo de teclado para eliminar tarea (D)
root.bind("<Escape>", close_application)  # Atajo de teclado para cerrar la aplicación (Escape)

# Iniciar la aplicación
root.mainloop()


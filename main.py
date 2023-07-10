import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))

def exit_editor():
    window.destroy()

window = tk.Tk()
window.title("Простой текстовый редактор")

# Создаем текстовое поле
text = tk.Text(window)
text.pack()

# Создаем меню
menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_editor)
menu_bar.add_cascade(label="Файл", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()

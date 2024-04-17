import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def read_csv_file(file_path):
    """Чтение CSV-файла и возврат данных в виде списка списков."""
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = [row for row in csv_reader]
        return data

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            parsed_data = read_csv_file(file_path)
            file_label.config(text="Имя файла: " + file_path)
            display_data(parsed_data)
        except FileNotFoundError:
            file_label.config(text="Файл не найден.")

def display_data(data):
    # Очистка таблицы перед отображением новых данных
    for i in tree.get_children():
        tree.delete(i)
    # Устанавливаем заголовки столбцов из первой строки данных
    if data:
        columns = data[0]
        tree["columns"] = tuple("#" + str(i) for i in range(len(columns)))
        for i, column in enumerate(columns):
            tree.heading("#" + str(i), text=column)
            tree.column("#" + str(i), width=100, stretch=True)
    # Вставка новых данных в таблицу, начиная со второй строки
    for row in data[1:]:
        tree.insert("", "end", values=row)

# Создание окна
root = tk.Tk()
root.title("Отображение данных CSV")

# Создание и настройка виджета таблицы
tree = ttk.Treeview(root)
tree.pack(fill="both", expand=True)

# Кнопка для выбора файла
open_button = tk.Button(root, text="Выбрать файл", command=open_file)
open_button.pack(pady=10)

# Метка для отображения имени файла
file_label = tk.Label(root, text="")
file_label.pack()

root.mainloop()

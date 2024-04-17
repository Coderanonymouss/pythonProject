import csv
import tkinter as tk
from tkinter import filedialog

def read_csv_file(file_path):
    """Чтение CSV-файла и возврат данных в виде списка словарей."""
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        # Читаем первую строку для получения заголовков колонок
        headers = next(csv_reader)
        # Читаем остальные строки и формируем список словарей
        data = [{header: value for header, value in zip(headers, row)} for row in csv_reader]
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
    for row in data:
        text_box.insert(tk.END, row)
        text_box.insert(tk.END, '\n')

# Создание окна
root = tk.Tk()
root.title("Чтение CSV файла")

# Кнопка для выбора файла
open_button = tk.Button(root, text="Выбрать файл", command=open_file)
open_button.pack(pady=10)

# Метка для отображения имени файла
file_label = tk.Label(root, text="Имя файла: ")
file_label.pack()

# Текстовое поле для вывода содержимого файла
text_box = tk.Text(root, width=50, height=20)
text_box.pack()

root.mainloop()

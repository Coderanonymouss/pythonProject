# Подключаем библиотеки, которые позволяют нам работать с данными и создавать графические интерфейсы
import pandas as pd  # Библиотека для работы с данными, похожа на Excel
import tkinter as tk  # Библиотека для создания графических интерфейсов
from tkinter import ttk  # Набор графических элементов для Tkinter
from functools import partial
# Создаем данные для таблицы с информацией о людях
data = {
    'First Name': ['John', 'Mary', 'Alex', 'Helen', 'Paul', 'Anna', 'David', 'Natalie', 'Serge', 'Olivia',
                   'Arthur', 'Tanya', 'Michael', 'Julia', 'Constantine', 'Catherine', 'Alexandra', 'Andrew', 'Linda', 'Gregory'],
    'Last Name': ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
                  'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70,
            75, 80, 85, 90, 95, 100, 105, 110, 115, 120],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
             'Austin', 'Jacksonville', 'San Francisco', 'Indianapolis', 'Seattle', 'Denver', 'Washington', 'Boston', 'El Paso', 'Detroit'],
    'Country': ['USA', 'RUS', 'KAZ', 'USA', 'UZB', 'USA', 'UZB', 'KAZ', 'USA', 'UZB',
                'KAZ', 'USA', 'RUS', 'UZB', 'RUS', 'KAZ', 'RUS', 'UZB', 'KAZ', 'KAZ']
}

# Создаем таблицу из данных
df = pd.DataFrame(data)

# Создаем функцию для обработки поиска
def handle_search(*args):
    query = search_var.get().lower()  # Получаем запрос из поля ввода и переводим в нижний регистр
    result_df = df[df.apply(lambda row: any(query in str(cell).lower() for cell in row), axis=1)]  # Фильтруем данные в таблице
    update_table(result_df)  # Обновляем таблицу с результатами поиска

# Создаем функцию для обновления таблицы
def update_table(result_df):
    tree.delete(*tree.get_children())  # Очищаем текущие данные в таблице

    # Вставляем новые данные в таблицу
    for index, row in result_df.iterrows():
        tree.insert('', 'end', values=row.to_list())

# Создаем главное окно программы
root = tk.Tk()
root.title("Search")  # Задаем заголовок окна

# Создаем поле для ввода запроса
search_var = tk.StringVar()  # Переменная для хранения текста из поля ввода
search_var.trace("w", handle_search)  # Связываем функцию обработки поиска с изменением текста в поле ввода
search_entry = ttk.Entry(root, textvariable=search_var)  # Создаем поле ввода с использованием ttk, чтобы оно выглядело красивее
search_entry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')  # Размещаем поле ввода на главном окне программы

# Создаем таблицу для отображения данных
columns = list(df.columns)  # Получаем названия столбцов из таблицы
tree = ttk.Treeview(root, columns=columns, show='headings')  # Создаем таблицу с названиями столбцов
for col in columns:
    tree.heading(col, text=col)  # Задаем названия столбцов
tree.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')  # Размещаем таблицу на главном окне программы

# Добавляем возможность прокрутки таблицы
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)  # Создаем вертикальный скроллбар
scrollbar.grid(row=1, column=1, sticky='ns')  # Размещаем скроллбар
tree.configure(yscrollcommand=scrollbar.set)  # Связываем скроллбар с таблицей

# Заполняем таблицу начальными данными
update_table(df)

# Запускаем главный цикл программы
root.mainloop()

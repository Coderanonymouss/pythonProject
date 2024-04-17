import pandas as pd
import tkinter as tk
from tkinter import ttk

# Create a DataFrame with 5 columns and 20 rows
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

df = pd.DataFrame(data)


def handle_search(*args):
    query = search_var.get().lower()
    column_to_search = column_var.get()

    # Check if the column is of string type before using .str.lower()
    if df[column_to_search].dtype == 'object':
        result_df = df[df[column_to_search].str.lower().str.contains(query)]
    else:
        result_df = df[df[column_to_search].astype(str).str.lower().str.contains(query)]

    update_table(result_df)


# Функция для обновления таблицы
def update_table(result_df):
    # Очистить текущие данные в таблице
    tree.delete(*tree.get_children())

    # Вставить новые данные в таблицу
    for index, row in result_df.iterrows():
        tree.insert('', 'end', values=row.to_list())

# Create the main window
root = tk.Tk()
root.title("Search by Column")

# Create a field for entering a query
search_var = tk.StringVar()
search_var.trace("w", handle_search)
search_entry = ttk.Entry(root, textvariable=search_var)
search_entry.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

# Create a dropdown menu for selecting column
columns = list(df.columns)
column_var = tk.StringVar()
column_menu = ttk.OptionMenu(root, column_var, columns[0], *columns)
column_menu.grid(row=0, column=1, padx=10, pady=10)

# Create a table
columns = list(df.columns)
tree = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

# Configure table scrolling
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=1, column=2, sticky='ns')
tree.configure(yscrollcommand=scrollbar.set)

# Populate the table with initial data
update_table(df)

# Start the main loop
root.mainloop()

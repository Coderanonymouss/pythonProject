import csv


def read_csv_file(file_path):
    """Чтение CSV-файла и возврат данных в виде списка словарей."""
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        # Читаем первую строку для получения заголовков колонок
        headers = next(csv_reader)
        # Читаем остальные строки и формируем список словарей
        data = [{header: value for header, value in zip(headers, row)} for row in csv_reader]
        return data


# Пример использования:
file_path = 'example.csv'
parsed_data = read_csv_file(file_path)

for row in parsed_data:
    print(row)

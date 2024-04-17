import requests

# Функция для отправки сетевого запроса
def send_request(url):
    try:
        response = requests.get(url)
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return 0, str(e)

# Функция для обработки результатов запроса
def process_response(status_code, content):
    if status_code == 200:
        print("Запрос выполнен успешно. Содержимое:")
        print(content)
    else:
        print("Произошла ошибка при выполнении запроса. Код ошибки:", status_code)
        print("Сообщение об ошибке:", content)

# Функция для выполнения мониторинга сети
def network_monitoring(url):
    status_code, content = send_request(url)
    process_response(status_code, content)

# Пример использования
if __name__ == "__main__":
    url = "https://www.example.com"
    network_monitoring(url)

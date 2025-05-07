import requests

def check_url(url):
    """Проверяет URL и обрабатывает ответ"""
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code < 400: 
            print(f"Успех: {url}\nКод: {response.status_code}\nОтвет: {response.text}\n")
        else: 
            raise Exception(f"Ошибка: {url}\nКод: {response.status_code}\nОтвет: {response.text}")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка запроса: {url}\nПричина: {str(e)}")

if __name__ == "__main__":
    # Тестовые URL
    urls = [
        "https://httpstat.us/100",
        "https://httpstat.us/200", 
        "https://httpstat.us/304",
        "https://httpstat.us/404",
        "https://httpstat.us/500"
    ]
    
    for url in urls:
        try:
            check_url(url)
        except Exception as e:
            print(f"Ошибка: {e}\n")
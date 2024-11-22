import requests
from datetime import datetime


def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Ошибка запроса: {response.status_code}")
            return None
    except Exception as e:
        print(f"Произошла ошибка при запросе: {e}")
        return None


def parse_wttr_weather():
    url = 'https://wttr.in/?format=%l:+%t'
    html = get_html(url)

    if not html:
        return "Не удалось получить данные о погоде."


    data = html.strip().split(': ')
    location = data[0]
    temperature = data[1]

    return f"{location}: температура {temperature}"


weather = parse_wttr_weather()
print(weather)

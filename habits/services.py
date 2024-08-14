import requests
from django.conf import settings


def send_telegram_message(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    try:
        response = requests.get(
            f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage",
            params=params,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        # Логирование ошибки
        print(f"Error sending message: {e}")

from celery import shared_task
from datetime import datetime, timedelta
from .models import Habit
from .services import send_telegram_message


@shared_task
def send_habit_reminders():
    habits = Habit.objects.all()
    for habit in habits:
        periodicity = habit.periodicity.all()
        chat_id = habit.user.tg_chat_id
        for period in periodicity:
            if (
                (
                    period.name == datetime.now().strftime("%a").upper()
                    or period.period == "DAILY"
                )
                and habit.start_at.hour == datetime.now().hour
                and habit.start_at.minute == datetime.now().minute
            ):
                message = f"Время начать: {habit.action}"
                send_telegram_message(chat_id=chat_id, message=message)

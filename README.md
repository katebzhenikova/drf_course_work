ПРИВЫЧКИ - это приложение для рассылки в телеграм напоминаний от бота
о полезных привычках по расписанию пользователя.
Описание:
Пользователь после регистрации или авторизации может создать свою полезную привычку.
В ней он указывает время, дни недели(или ежедневно), в которые хочет, чтобы ему приходило напоминание от бота, 
что пора приступить к привычке.

Эндпоинты:

Регистрация
http://localhost:8000/users/register/

Авторизация
http://localhost:8000/users/token/

Список пользователей (только для админа)
http://localhost:8000/users/user_list/

Список привычек текущего пользователя с пагинацией
http://localhost:8000/habits/

Список публичных привычек
http://localhost:8000/habits/public_list/

Создание привычки
http://localhost:8000/habits/create/

Редактирование привычки
http://localhost:8000/habits/update/<int:pk>/

Удаление привычки
http://localhost:8000/habits/delete/<int:pk>/

Модели:
Habit, HabitPeriodicity, User

Сохранение результатов проверки покрытия тестами.
pip install coverage 
coverage run manage.py test 
coverage report -m > coverage_report.txt
В файле coverage_report.txt сохранены результаты тестов

для запуска задач отправки сообщений в телеграм на Windows
pip install redis 
Запустить redis из cmd C:\Redis> redis-server.exe
pip install celery (+ настройки в settings.py, __init__)
pip install eventlet 
pip install django-celery-beat  
celery -A config worker -l INFO -P eventlet
celery -A config beat --scheduler django --loglevel=info
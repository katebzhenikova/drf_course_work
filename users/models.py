from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта пользователя")
    phone = models.CharField(
        max_length=35, verbose_name="телефон пользователя", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/", verbose_name="аватар пользователя", **NULLABLE
    )
    tg_nick = models.CharField(
        max_length=50, verbose_name="никнэйм телеграмм", **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=50, verbose_name="телеграмм ID", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

from django.db import models
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from config import settings
from users.models import User


class HabitPeriodicity(models.Model):
    DAY_OF_WEEK_CHOICES = (
        ("MON", "Понедельник"),
        ("TUE", "Вторник"),
        ("WED", "Среда"),
        ("THU", "Четверг"),
        ("FRI", "Пятница"),
        ("SAT", "Суббота"),
        ("SUN", "Воскресенье"),
    )

    PERIOD_CHOICES = (
        ("DAILY", "Ежедневно"),
        ("WEEKLY", "Еженедельно"),
    )

    name = models.CharField(
        max_length=50, choices=DAY_OF_WEEK_CHOICES, null=True, blank=True
    )
    period = models.CharField(
        max_length=50, choices=PERIOD_CHOICES, null=True, blank=True
    )

    def __str__(self):
        if self.name:
            return self.get_name_display()
        elif self.period:
            return self.get_period_display()
        else:
            return ""


class Habit(models.Model):
    """Модель Привычка"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="Пользователь",
    )
    place = models.CharField(max_length=255, verbose_name="Место")
    action = models.CharField(max_length=255, verbose_name="Действие")
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    related_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
    )
    periodicity = models.ManyToManyField(
        HabitPeriodicity, max_length=50, verbose_name="периодичность"
    )

    reward = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Вознаграждение"
    )
    estimated_time = models.DurationField(
        null=True, blank=True, verbose_name="Время на выполнение"
    )
    start_at = models.TimeField(verbose_name="Время начала выполнения")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")

    def __str__(self):
        return f"{self.action} ({self.user.email})"

    def clean(self):
        if self.related_habit and self.reward:
            raise ValidationError(
                _(
                    "Нельзя указать одновременно связанную привычку и вознаграждение. Можно заполнить только одно из этих полей."
                )
            )
        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError(
                _(
                    "У приятной привычки не может быть вознаграждения или связанной привычки."
                )
            )

    def get_periodicity(self):
        return ", ".join([str(p) for p in self.periodicity.all()])

    get_periodicity.short_description = "Периодичность"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

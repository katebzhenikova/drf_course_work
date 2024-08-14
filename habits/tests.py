import pytest
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User

from habits.models import Habit, HabitPeriodicity
from habits.serializers import HabitSerializer
from datetime import datetime, timedelta, time
from django.contrib.auth import get_user_model
from .tasks import send_habit_reminders
from .services import send_telegram_message


User = get_user_model()


class HabitAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="user@example.com")
        self.periodicity1 = HabitPeriodicity.objects.create(name="Ежедневно")
        self.periodicity2 = HabitPeriodicity.objects.create(name="Еженедельно")

        self.habit = Habit.objects.create(
            place="Habit Test place",
            action="Test Habit action",
            user=self.user,
            is_public=False,
            start_at=time(12, 30),
            reward="Test reward",
        )
        self.habit.periodicity.set([self.periodicity1, self.periodicity2])

        self.public_habit = Habit.objects.create(
            place="Public Test Habit",
            action="Public Test Habit Description",
            user=self.user,
            is_public=True,
            start_at=time(12, 30),
            reward="Test reward",
        )
        self.public_habit.periodicity.set([self.periodicity1, self.periodicity2])

        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "place": "Habit Test place",
            "action": "Test Habit action",
            "is_public": False,
            "start_at": "12:30:00",
            "reward": "Test reward",
            "periodicity": [self.periodicity1.id, self.periodicity2.id],
            "user": self.user.id,
        }
        response = self.client.post(
            reverse("habits:habits-create"), data, format="json"
        )
        print(response.data)  # Добавьте эту строку для вывода ошибок
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Habit.objects.count(), 3)

    def test_habit_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("habits:habits-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 2)

    def test_habit_retrieve(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse("habits:habits-detail", kwargs={"pk": self.habit.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["action"], self.habit.action)

    def test_habit_update(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "place": "Habit Test place",
            "action": "Test Habit action",
            "is_public": False,
            "start_at": "12:30:00",
            "reward": "Test reward",
            "periodicity": [self.periodicity1.id, self.periodicity2.id],
            "user": self.user.id,
        }
        response = self.client.put(
            reverse("habits:habits-update", kwargs={"pk": self.habit.pk}), data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Habit.objects.get(pk=self.habit.pk).action, "Test Habit action"
        )

    def test_habit_destroy(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse("habits:habits-delete", kwargs={"pk": self.habit.pk})
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Habit.objects.count(), 1)

    def test_habit_public_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("habits:habits-public-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    HabitPublicListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habits-list"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habits-create"),
    path(
        "habits/public_list/",
        HabitPublicListAPIView.as_view(),
        name="habits-public-list",
    ),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits-detail"),
    path("habits/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habits-update"),
    path(
        "habits/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habits-delete"
    ),
]

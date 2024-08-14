from rest_framework import serializers
from .models import Habit, HabitPeriodicity


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"


class HabitPeriodicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitPeriodicity
        fields = "__all__"

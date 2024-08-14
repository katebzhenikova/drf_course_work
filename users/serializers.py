from rest_framework import serializers

from habits.serializers import HabitSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    habits = HabitSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

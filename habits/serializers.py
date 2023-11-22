from rest_framework import serializers

from habits.models import Habits
from habits.validators import validate_related_habit, validate_estimated_time, validate_rewarding_habit, \
    validate_frequency, validate_notification_time


class HabitsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habits.
    """

    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, data):
        """
        Валидаторы для модели Habits.
        """
        validate_related_habit(data)
        validate_estimated_time(data)
        validate_rewarding_habit(data)
        validate_frequency(data)
        validate_notification_time(data)
        return data

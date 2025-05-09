from rest_framework import serializers
from .models import Reminder
from datetime import datetime

class ReminderSerializer(serializers.ModelSerializer):
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)

    class Meta:
        model = Reminder
        fields = ['date', 'time', 'message', 'reminder_type', 'reminder_datetime']
        read_only_fields = ['reminder_datetime']

    def create(self, validated_data):
        date = validated_data.pop('date')
        time = validated_data.pop('time')
        reminder_datetime = datetime.combine(date, time)
        validated_data['reminder_datetime'] = reminder_datetime
        return Reminder.objects.create(**validated_data)

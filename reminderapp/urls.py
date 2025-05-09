from django.urls import path
from .views import ReminderCreateView

urlpatterns = [
    path('api/reminders/', ReminderCreateView.as_view(), name='create-reminder'),
]

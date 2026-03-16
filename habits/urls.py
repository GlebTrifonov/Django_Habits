from django.urls import path
from .views import habit_list, habit_create

urlpatterns = [
    path('', habit_list, name='habit_list'),
    path('create/', habit_create, name='habit_create')
]
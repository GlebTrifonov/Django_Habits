from django.urls import path
from .views import habit_list, habit_create, habit_toggle, habit_delete

urlpatterns = [
    path('', habit_list, name='habit_list'),
    path('create/', habit_create, name='habit_create'),
    path('<int:pk>/toggle/', habit_toggle, name='habit_toggle'),
    path('<int:pk>/delete/', habit_delete, name='habit_delete'),
]
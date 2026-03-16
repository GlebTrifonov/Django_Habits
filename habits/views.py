from django.shortcuts import render
from .models import Habit

def habit_list(request):
    habits = Habit.objects.all()
    context = {
        'my_habits': habits,
        'title': 'Мой список привычек',
    }
    return render(request, 'habits/habit_list.html', context)
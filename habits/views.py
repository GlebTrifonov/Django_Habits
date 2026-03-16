from django.shortcuts import render, redirect
from .models import Habit
from django.contrib.auth.decorators import login_required
from .forms import HabitForm


@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    context = {
        'my_habits': habits,
        'title': 'Мой список привычек',
    }
    return render(request, 'habits/habit_list.html', context)


@login_required
def habit_create(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    
    context = {
        "form": form
    }

    return render(request, 'habits/habit_form.html', context)
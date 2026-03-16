from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('habit_list')
    return render(request, 'users/home.html')



from django.contrib import admin
from .models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'is_completed')
    list_filter = ('is_completed', 'user')
    search_fields = ('title', 'description')

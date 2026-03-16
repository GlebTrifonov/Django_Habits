from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer

class HabitListAPIView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
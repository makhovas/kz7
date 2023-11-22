from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .models import Habits
from .paginations import HabitsPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import HabitsSerializer


class HabitsListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и просмотра списка привычек пользователя.
    """
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = HabitsPagination

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habits.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Автоматически устанавливаем пользователя при создании привычки
        serializer.save(user=self.request.user)


class HabitsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления привычки.
    """
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habits.objects.filter(user=self.request.user)


class PublicHabitsListView(generics.ListAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

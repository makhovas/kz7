from django.urls import path
from .views import HabitsListCreateView, HabitsDetailView, PublicHabitsListView

urlpatterns = [
    path('habits/', HabitsListCreateView.as_view(), name='habits-list-create'),
    path('habits/<int:pk>/', HabitsDetailView.as_view(), name='habits-detail'),
    path('habits/public/', PublicHabitsListView.as_view(), name='habits-public'),
]

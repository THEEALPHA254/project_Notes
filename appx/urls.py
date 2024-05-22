# urls.py
from django.urls import path
from . import views  # Assuming your views.py is in the same directory

urlpatterns = [
    path('notes/', views.NoteView.as_view()),
]
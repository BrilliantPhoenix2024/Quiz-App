from django.urls import path

from .views import Quiz

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_viwe(), name='quiz'),
]

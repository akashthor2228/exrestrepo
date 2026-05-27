from django.urls import path
from restapp import views
from restapp.views import StudentAPI

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', StudentAPI.as_view()),
]
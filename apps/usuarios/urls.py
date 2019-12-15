from django.urls import path
from .views import *

urlpatterns = [
    path('', Login.as_view()),
    path('home', Home.as_view()),
]
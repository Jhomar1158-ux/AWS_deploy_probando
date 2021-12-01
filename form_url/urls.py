from django.urls import path
from form_url import views

urlpatterns = [
    path('random_word/', views.index),
    path('reset/', views.reset)
]

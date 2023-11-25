from django.urls import path
from .tickets import views

urlpatterns = [
    path('tickets/', views.CreateTicket.as_view()),
    path('tickets/<pk>/', views.RetrieveTicket.as_view()),
]

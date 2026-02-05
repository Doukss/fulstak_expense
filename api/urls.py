
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("transactions/", views.TransactCreateView.as_view()),
    path("transactions/<int:id>/", views.TransactionRetrieveUpdateDestroyView.as_view())
    
]

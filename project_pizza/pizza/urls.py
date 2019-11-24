from django.urls import path
from . import views

urlpatterns = [
    path('', views.PizzaHomeView.as_view()),
    path('pizza-form-add/', views.PizzaFormAddView.as_view(),),
    path('pizza-update/<int:pk>/edit/', views.PizzaUpdateView.as_view(),),
]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from values import views

urlpatterns = [
    path('', views.ValuesList.as_view()),
    path('<int:pk>/', views.ValuesDetail.as_view()),
]

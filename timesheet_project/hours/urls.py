from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hours import views

urlpatterns = [
    path('', views.HoursList.as_view()),
    path('<int:pk>/', views.HoursDetail.as_view()),
]

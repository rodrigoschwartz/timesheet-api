from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hours import views

urlpatterns = [
    path('', views.HoursListByUser.as_view()),
    path('create/', views.HoursCreate.as_view())
]

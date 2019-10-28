from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from values import views

urlpatterns = [
    path('', views.ValuesListByUser.as_view()),
    path('create/', views.ValuesCreate.as_view()),
    path('delete/', views.ValuesDelete.as_view()),
]

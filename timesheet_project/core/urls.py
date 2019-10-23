from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('user/', views.ProjectListByUser.as_view()),
    path('create/', views.ProjectCreate.as_view()),
    path('delete/', views.ProjectDelete.as_view()),
    path('update/', views.ProjectUpdate.as_view()),
]

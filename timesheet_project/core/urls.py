from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('', views.ProjectListAll.as_view()),
    path('user/', views.get_proj, name="Projects"),
    path('<int:pk>/', views.ProjectDetail.as_view()),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from core import views

urlpatterns = [
    path('projects/', include('core.urls')),
    path('values/', include('values.urls')),
    path('hours/', include('hours.urls')),
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),
    path('auth/', obtain_auth_token, name='api_token_auth') ]
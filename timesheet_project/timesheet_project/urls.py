from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('projects/', include('core.urls')),
    path('values/', include('values.urls')),
    path('hours/', include('hours.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from . import views

#incluindo faculdade e comercio
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('faculdade/', include('faculdade.urls')),
    path('comercio/', include('comercio.urls'))
]

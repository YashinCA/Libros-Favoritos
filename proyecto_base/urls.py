from django.contrib import admin
from django.urls import path
from django.urls import include
from decorator_include import decorator_include
from acceso.utils.decoradores import login_requerido

urlpatterns = [
    path('',  decorator_include(login_requerido, include('core.urls'))),
    path('acceso/', include('acceso.urls')),
    path('admin/', admin.site.urls),
]

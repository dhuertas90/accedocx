"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importar views
from app.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    
    path('documentos/', views.documentos, name='documentos'),
    path('documentos/subir/', views.seccion_subir_documento, name='seccion_subir_documento'),
    path('documentos/subir/doc', views.upload_documento, name='upload_documento'),
    path('documentos/<int:pk>/', views.delete_documento, name='delete_documento'),

    path('accesibilizando/<int:pk>/', views.get_documento, name='get_documento'),
    path('convertir/', views.convertir, name='convertir'),
    
    path('pdf/', views.seccion_convertir_pdf, name='seccion_convertir_pdf'),
    path('pdf/convertir', views.convert_to_docx, name='convert_to_docx'),
    path('realizar_conversion/', views.realizar_conversion, name='realizar_conversion'),

    # Implementación futura
    path('docx_a_pdf/<int:pk>', views.convert_to_pdf, name='convertir_a_pdf'),

]
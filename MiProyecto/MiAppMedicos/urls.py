"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from MiAppMedicos import views
from .views import medico_view

urlpatterns = [  
    path('', views.portada, name="Portada"),
    path('BMVBCMedicos/', views.MedicoModelsListView.as_view(), name = "EditaBorra"),
    path('Editar/<int:MedicoModels_id>/', views.editamedico, name = "EditaMedico"),
    path('Borrar/<int:MedicoModels_id>/', views.borramedico, name = "BorraMedico"),
    path('Secundario/', views.Secundario, name ="Secundario"),
]

formaltamedico_html = [
    path('alta-medico/', views.AltaMedico, name="AltasMedicos")
 
]
forms_api_medico =[
    path('ApiAltaMedico/',views.medico_view, name="AltaMed")
]

forms_api_paciente =[
    path('ApiAltaPaciente/',views.paciente_view, name="AltaPac")
]

CargaContultaTurnos = [
    path('cargar_turno/', views.cargar_turno, name='cargar_turno'),
    path('consultar_turnos/', views.consultar_turnos, name='consultar_turnos'),
    
]

urlpatterns += formaltamedico_html + forms_api_medico + forms_api_paciente + CargaContultaTurnos 

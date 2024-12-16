from django.contrib import admin # type: ignore
from MiAppMedicos.models import MedicoModels
from MiAppMedicos.models import PacienteModels
from MiAppMedicos.models import Turno

# Register your models here.

admin.site.register(MedicoModels)
admin.site.register(PacienteModels)
admin.site.register(Turno)

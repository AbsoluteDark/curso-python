# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# Importar modelo
from documentos.models import Documentos
# Crear una sub-clase de admin.ModelAdmin
class DocumentoAdmin(admin.ModelAdmin):
	model = Documentos

# Registrar ModelAdmin para C/modelo
admin.site.register(Documentos, DocumentoAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# Las vistas manejan la logica del sitio web.
from django.views.generic import View

# Metodo render retorna una respuesta
# Combina una plantilla con un diccionary of contexto
# Y retorna un objeto HttpResponse
from django.shortcuts import render
from documentos.models import Documentos as ModeloDocumentos

class Documentos(View):
	def get(self, request, *args, **kwargs):
		
		docs = ModeloDocumentos.objects.all()
		context = {
		'docs': docs,
		'encabezado': 'Mys owns Documents'
		}

		return render(
			request, 
			'documentos.html', 
			context
			)
	
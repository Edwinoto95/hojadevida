import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render

def inicio(request):
    # Solo renderiza la plantilla, el contenido es estático
    return render(request, 'inicio.html')

def descargar_pdf_estatico(request):
    # Cambia el nombre del archivo si es necesario
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', 'DaniloOto.pdf')
    if os.path.exists(pdf_path):
        response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Danilo-Oto.pdf"'
        return response
    else:
        raise Http404("El archivo PDF no existe.")


from django.shortcuts import render

def experiencia(request):
  
    return render(request, 'experiencia.html')


from django.shortcuts import render

def educacion(request):
    return render(request, 'educacion.html')


from django.shortcuts import render

def habilidades(request):
    return render(request, 'habilidades.html')


from django.shortcuts import render

def tecnologias(request):
    return render(request, 'tecnologias.html')

from django.shortcuts import render

def proyectos(request):
    return render(request, 'proyectos.html')

from django.urls import path
from . import views

app_name = 'vida'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('descargar-pdf/', views.descargar_pdf_estatico, name='descargar_pdf_estatico'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('educacion/', views.educacion, name='educacion'),
    path('habilidades/', views.habilidades, name='habilidades'),
    path('tecnologias/', views.tecnologias, name='tecnologias'),
    path('proyectos/', views.proyectos, name='proyectos'),  # nueva ruta
]

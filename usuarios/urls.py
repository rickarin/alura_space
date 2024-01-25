from django.urls import path
from usuarios.views import login, cadastro
from galeria.views import index

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro')
]

from django.urls import path
from . import views

urlpatterns =[
    path("nova_loja", views.Cadastro_Loja, name='nova_loja'),
]
from django.urls import path

#enxergando o arquivo de views
from . import views

# criando uma váriavel (lista) que pode ser alterada 
urlpatterns = [ #controler que fica monitorando qual url o usuário está utilizando - redireciona a requisição do usuário para a view específica
    path('', views.index, name='index'), 
    path('mabou', views.mabou, name='mabou'), 
]


# em uma exprsssão regular você consegue fazer pesquisas em textos
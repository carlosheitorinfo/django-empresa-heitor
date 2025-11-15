from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('produtos/',views.produtos, name='produtos'),
    path('clientes/',views.clientes, name='clientes'),
    path('funcionarios/',views.funcionarios, name='funcionarios'),
    path('contato/', views.formulario_contato_view, name='contatos'),
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view ,name='logout'),
    path('perfil/',views.perfil ,name='perfil'),
    path('registrar/',views.registrar_view ,name='registrar'),
    
]
    



from django.urls import path
from .views import login_view,logout_view,inicio_view,ingresar_guara,enviar_whatsapp_directo,ver_categoria,test_db

urlpatterns = [
    path('', inicio_view, name="inicio"),
    path('test/', test_db, name='test_db'),
    path('login/', login_view, name="login_guara"),
    path('ingresar_guara', ingresar_guara, name="ingresar_guara"),
    path('enviar-whatsapp', enviar_whatsapp_directo, name='enviar_whatsapp'),
    path('ver_categoria', ver_categoria, name='ver_categoria'),
   # path('register/', register_user, name="register"),
    path("logout/", logout_view, name="logout")

]

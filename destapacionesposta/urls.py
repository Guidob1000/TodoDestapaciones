from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register("User" , views.UserView)
router.register("Direccion" , views.DireccionView)
router.register("Camioneta" , views.CamionetaView)
router.register("Trabajador" , views.TrabajadorView)
router.register("Administracion" , views.AdministracionView)
router.register("Ratings" , views.RatingsView)
router.register("Pedidos_Register" , views.Pedidos_RegisterView)



urlpatterns = [
    #path('admin/', admin.site.urls),
    path ("" , include (router.urls)),
   
]
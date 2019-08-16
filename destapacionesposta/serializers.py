from rest_framework import serializers
from .models import User , Camioneta , Direccion , Trabajador , Administracion , Ratings , Pedidos_Register


class AdministracionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Administracion
		fields = ("id" , "mail" , "id_direccion_admin" , "telefono")

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ("id" , "nombre", "url" , "apellido" , "contraseña" , "mail" ,  "id_direccion" , "nacimiento"  , "telefono")
	
	
class DireccionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Direccion
		fields = ("id" , "piso" , "calle" , "numero_calle" , "telefono" , "id_administracion")

class TrabajadorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Trabajador
		fields = ("id" , "nombre" , "apellido" , "rating")

class RatingsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ratings
		fields = ("trabajador1" , "Rating_general" , "Rating_numers" , "Cant_Rating")

class CamionetaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Camioneta
		fields =("id" , "patente_letra" , "patente_numero")

class Pedidos_RegisterSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Pedidos_Register
		fields = ("id" , "id_usuario" , "id_trabajador" , "id_camioneta" , "id_direccion" , "fecha" , "rating")


		
		

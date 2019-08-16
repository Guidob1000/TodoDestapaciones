from django.db import models

class Direccion(models.Model):
		piso = models.CharField(max_length=50 , null=True)
		calle = models.CharField(max_length=50)
		telefono = models.CharField(max_length=50)
		numero_calle = models.CharField(max_length=50)
		id_administracion = models.ForeignKey('Administracion', on_delete=models.CASCADE , null=True)
		
class Trabajador(models.Model):
		nombre = models.CharField(max_length=50)
		apellido = models.CharField(max_length=50)
		rating = models.ForeignKey("Ratings", on_delete=models.CASCADE , null=True)

class Ratings(models.Model):
		trabajador1 = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
		Rating_general = models.CharField(max_length=50)
		Rating_numers = models.CharField(max_length=50)
		Cant_Rating = models.CharField(max_length=50)

class Administracion(models.Model):
		mail = models.EmailField(max_length=50)
		telefono = models.CharField(max_length=50)
		id_direccion_admin = models.ManyToManyField(Direccion)
		

class Camioneta(models.Model):
		patente_letra = models.CharField(max_length=50)
		patente_numero = models.CharField(max_length=50)

class User(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	mail = models.EmailField(max_length=50)
	contraseña = models.CharField(max_length=50)
	id_direccion = models.ManyToManyField(Direccion)
	nacimiento = models.DateField(null=True, blank=True)
	telefono = models.CharField(max_length=50)

class Pedidos_Register(models.Model):
		
		id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
		id_trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
		id_camioneta = models.ForeignKey(Camioneta, on_delete=models.CASCADE)
		id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
		fecha = models.DateTimeField(blank=False, auto_now_add=True)
		rating = models.ForeignKey(Ratings, on_delete=models.CASCADE, default=1)








	#Tengo que crear una nueva tabla para los ratings asi , me va a ser mucho mas facil conectar con el pedidos register y tambien facilita a la hora de calcular los ratings.


	

		


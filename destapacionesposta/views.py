from django.shortcuts import render
from rest_framework import viewsets
from .models import User , Direccion , Trabajador , Camioneta , Administracion , Ratings , Pedidos_Register
from .serializers import UserSerializer , DireccionSerializer , RatingsSerializer , TrabajadorSerializer , CamionetaSerializer, AdministracionSerializer , Pedidos_RegisterSerializer
'''
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
'''
class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class DireccionView(viewsets.ModelViewSet):
	queryset = Direccion.objects.all()
	serializer_class = DireccionSerializer

class TrabajadorView(viewsets.ModelViewSet):
	queryset = Trabajador.objects.all()
	serializer_class = TrabajadorSerializer

class CamionetaView(viewsets.ModelViewSet):
	queryset = Camioneta.objects.all()
	serializer_class = CamionetaSerializer

class Pedidos_RegisterView(viewsets.ModelViewSet):
	queryset = Pedidos_Register.objects.all()
	serializer_class = Pedidos_RegisterSerializer

class AdministracionView(viewsets.ModelViewSet):
	queryset = Administracion.objects.all()
	serializer_class = AdministracionSerializer

class RatingsView(viewsets.ModelViewSet):
	queryset = Ratings.objects.all()
	serializer_class = RatingsSerializer
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from pycognito import Cognito

from django_cognito_jwt import JSONWebTokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

username = openapi.Parameter('username', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING, )
password = openapi.Parameter('password', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING, )


class LoginView(APIView):
    @swagger_auto_schema(manual_parameters=[username, password], responses={200: 'user_response'})
    def post(self, request, format=None):
        username = self.request.query_params.get('username')
        password = self.request.query_params.get('password')
        try:
            u = Cognito('ap-south-1_naR1NxJe2', '53cnie8g86gldjrg3hsknbuhck', username=username)
            u.authenticate(password=password)
            context = {'username': username,
                       'access_tokem': u.access_token,
                       'id_token': u.id_token,
                       'refresh_token': u.refresh_token
                       }
            return Response(context, status=200)
        except Exception as e:
            return Response({'message': str(e)}, status=400)


class ExampleView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {'message': 'success'}
        return Response(content)


# app_client_id: 53cnie8g86gldjrg3hsknbuhck
# app_secret_id:15gq5k6fgn4k0vbj08oiv3pmqvtot0cv453j99d4abqqc0p98skt
# pool_id:ap-south-1_naR1NxJe2

# Create your views here.
def home(request):
    return HttpResponse('Hello world')

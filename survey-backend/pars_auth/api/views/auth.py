from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from pars_auth.api.serializers import CustomTokenObtainPairSerializer
from django.utils import timezone


class EmailTokenObtainPairView(TokenObtainPairView):
    authentication_classes = []

    serializer_class = CustomTokenObtainPairSerializer


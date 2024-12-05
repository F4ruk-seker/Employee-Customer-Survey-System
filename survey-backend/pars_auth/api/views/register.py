from rest_framework.generics import CreateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from pars_auth.api.serializers import CreateUserSerializer
from rest_framework.views import Response
from rest_framework.views import APIView
from pars_auth.api.serializers import TempUserSerializer
from pars_auth.models import User, EmailConfirmation
from django.shortcuts import get_object_or_404


class RegisterView(CreateAPIView):
    authentication_classes = []
    serializer_class = CreateUserSerializer


class ConfirmUser(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        census_token = self.request.query_params.get('census_token')
        email_confirmation = get_object_or_404(EmailConfirmation,
                                               confirmation_token=token,
                                               census_token=census_token
                                               )
        return Response({}, status=self.get_token_status(email_confirmation.status))

    def post(self, *args, **kwargs):
        email_confirmation = get_object_or_404(EmailConfirmation,
                                               confirmation_token=kwargs.get('token'),
                                               census_token=self.request.data.get('census_token')
                                               )
        if email_confirmation.status == 'u':
            email_confirmation.status = 'c'
            email_confirmation.save()
            # set user active status (True)
            email_confirmation.user.is_active = True
            email_confirmation.user.save()
            return Response({}, status=201)
        return Response({}, status=self.get_token_status(email_confirmation.status))

    def delete(self, *args, **kwargs):
        email_confirmation = get_object_or_404(EmailConfirmation,
                                               confirmation_token=kwargs.get('token'),
                                               census_token=self.request.data.get('census_token')
                                               )
        if email_confirmation.status == 'u':
            email_confirmation.status = 'e'
            email_confirmation.save()
        return Response({}, status=self.get_token_status(email_confirmation.status))

    @staticmethod
    def get_token_status(status: str) -> int:
        token_status = {
            'c': 208,
            'u': 200,
            'e': 226
        }
        return token_status[status]


class GetLoginUserAPIView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user

    def get(self, *args, **kwargs):

        return Response(TempUserSerializer(self.request.user).data, status=200)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from pars_auth.models import User, BaseToken


class PasswordResetTokenManageView(APIView):
    authentication_classes = []

    def post(self, *args, **kwargs):
        if email := self.request.data.get('email'):
            if user := User.objects.filter(email=email.strip()).first():
                BaseToken.objects.create(
                    user=user,
                    token_type=BaseToken.TokenType.password_reset_token
                )
        return Response({}, status=200)

    def put(self, *args, **kwargs):
        password = self.request.data.get('password', None)
        repeat_password = self.request.data.get('repeat_password', None)
        reset_token = self.request.data.get('reset_token', None)
        census_token = self.request.data.get('census_token', None)
        if password == repeat_password and reset_token and census_token and census_token[:5] == 'PARS@' and len(census_token) == 145:
            token = get_object_or_404(
                BaseToken,
                confirmation_token=reset_token,
                token_type=BaseToken.TokenType.password_reset_token
            )
            if not token.used:
                token.user.set_password(password)
                token.used = True
                token.save()
                return Response({}, status=201)
            else:
                return Response({}, status=208)
        else:
            return Response({}, status=406)


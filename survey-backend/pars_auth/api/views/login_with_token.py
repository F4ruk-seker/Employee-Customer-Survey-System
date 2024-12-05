from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from pars_auth.models import User, BaseToken


class LoginWithToken(APIView):
    authentication_classes = []

    def post(self, *args, **kwargs):
        if email := self.request.data.get('email', None):
            user = get_object_or_404(User, email=email)
            BaseToken.objects.create(
                user=user,
                token_type=BaseToken.TokenType.login_with_token
            )
        return Response({}, status=201)

    def put(self, *args, **kwargs):
        if token := self.request.data.get('token'):
            base_token = get_object_or_404(
                BaseToken,
                confirmation_token=token,
                token_type=BaseToken.TokenType.login_with_token
            )
            base_token.used = True
            base_token.save()

            refresh_token = RefreshToken.for_user(base_token.user)
            return Response({
                'access': str(refresh_token.access_token),
                'refresh': str(refresh_token)
            }, status=200)
        else:
            return Response({}, status=404)

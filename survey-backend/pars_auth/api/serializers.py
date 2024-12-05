from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from pars_auth.models import User
from rest_framework import serializers


class PasswordValidator:
    def __init__(self, field_name):
        self.field_name = field_name

    def __call__(self, value):
        print(value)
        print(self)
        print(self.field_name)
        # if value != self.context['request'].data[self.field_name]:
        #     raise serializers.ValidationError(f"{self.field_name} and password must match.")


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD


class CreateUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40, required=False)
    # repeat_password = serializers.CharField(
    # max_length=80,
    # write_only=True,
    # validators=[PasswordValidator(field_name='password')]
    # )

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('username', 'email_confirmation')
        read_only_fields = (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
            'date_joined',
            'last_login',
            'email_confirmation'
        )
        extra_kwargs = {
            # 'security_question': {'write_only': True},
            # 'security_question_answer': {'write_only': True},
            'password': {'write_only': True}
        }


class TempUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()

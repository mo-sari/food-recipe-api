from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

user = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = user
        fields = ('id', 'email', 'name', 'password')

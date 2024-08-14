from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password','placeholder': 'Re-Password'}
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5,
                'style': {'input_type': 'password', 'placeholder': 'Password'}
            },
        }

    def create(self, validated_data):
        password2 = validated_data.pop('password2', None)
        if not validated_data['password'] == password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})
        """Create a new user with encrypted password and return it"""
        return User.objects.create_user(**validated_data)




class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name', 'phone']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'phone']


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         token['email'] = user.email
#         # ...

#         return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     """
#     Takes a set of user credentials and returns an access and refresh JSON web
#     token pair to prove the authentication of those credentials.
#     """

#     serializer_class = MyTokenObtainPairSerializer


# class TokenSerializer(BaseTokenSerializer):
#     class Meta(BaseTokenSerializer.Meta):
#         fields = ['username', 'email', 'first_name', 'last_name']

# class TokenCreateSerializer(BaseTokenCreateSerializer):
#     class Meta(BaseTokenSerializer.Meta):
#         fields = ['username', 'email', 'first_name', 'last_name']

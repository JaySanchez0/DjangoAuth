from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import exceptions
from . import models
class AuthApp(authentication.BaseAuthentication):
    def authenticate(self, request):
        print(request.headers)
        #raise exceptions.AuthenticationFailed('')
        return (models.User('Juan',13),None)
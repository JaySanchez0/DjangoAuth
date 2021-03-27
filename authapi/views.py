from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from .AuthApp import AuthApp
from .permissions import AuthorPermission,PeoplePermission
@api_view(['GET'])
def index(request):
    return Response(data='Hola Mundo')

@api_view(['GET'])
@authentication_classes([AuthApp])
@permission_classes([
    #AuthorPermission,
    PeoplePermission
    ])
def secret(request):
    print(request.user.name)
    return Response(data=request.user.name)
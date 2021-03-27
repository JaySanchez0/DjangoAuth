# Django Rest Authentication

## Create Project

~~~
    django-admin startproject project-name
~~~

## Create App

~~~
    python manage.py startapp appname
~~~

## Setting rest framework

File settings.py add rest_framework and ConfigAppClass

~~~
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appname.apps.AppConfigClass',
    'rest_framework'
]
~~~

AppConfigClass is the name of class into apps file

## Write security
    Create a class who heritage BaseAuthentication

~~~
    class AuthApp(authentication.BaseAuthentication):
        def authenticate(self, request):
            print(request.headers)
            #raise exceptions.AuthenticationFailed('')
            return (models.User('Juan',13),None)
~~~
the exception send response 403 unauthorized

## Define Permission

We define a permission heritage class BasePermission

~~~
    class PeoplePermission(BasePermission):
        def has_permission(self, request, view):
            return true
~~~

When we put many permissions a route, all should return true from request response a result

## Routes secures

~~~

@api_view(['GET'])
@authentication_classes([AuthApp])
@permission_classes([ AuthorPermission,PeoplePermission])
def secret(request):
    print(request.user.name)
    return Response(data=request.user.name)

~~~
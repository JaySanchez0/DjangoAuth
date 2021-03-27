from rest_framework.permissions import BasePermission

class AuthorPermission(BasePermission):
    def has_permission(self, request, view):
        print(">>>>>>>>> Permision")
        print(request.user.name)
        return request.user.name=="Jorge"


class PeoplePermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.name)
        return request.user.name=="Juan"
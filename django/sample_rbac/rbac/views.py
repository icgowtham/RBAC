from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from rest_framework import generics

from rbac.models import Users, Roles, Resources, Actions, Role_Permission, User_Roles
from rbac.serializers import UserSerializer, RoleSerializer, ResourceSerializer, ActionSerializer, RolePermissionSerializer, UserRoleSerializer

# Create your views here.
def index(request):
    users_list = Users.objects.all()
    roles_list = Roles.objects.all()
    resources_list = Resources.objects.all()
    actions_list = Actions.objects.all()
    role_permission_list = Role_Permission.objects.all()
    user_roles_list = User_Roles.objects.all()

    template = loader.get_template('rbac/index.html')
    context = RequestContext(request, {
        'users_list': users_list,
        'roles_list': roles_list,
        'resources_list': resources_list,
        'actions_list': actions_list,
        'role_permission_list': role_permission_list,        
        'user_roles_list': user_roles_list,
    })
    return HttpResponse(template.render(context))   

# Users
class UsersList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer


# Roles
class RolesList(generics.ListCreateAPIView):
    """
    List all roles, or create a new role.
    """
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer

class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a role.
    """
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer


# Resources
class ResourcesList(generics.ListCreateAPIView):
    """
    List all resources, or create a new resource.
    """
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a resource.
    """
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer


# Actions
class ActionsList(generics.ListCreateAPIView):
    """
    List all actions, or create a new action.
    """
    queryset = Actions.objects.all()
    serializer_class = ActionSerializer

class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an action.
    """
    queryset = Actions.objects.all()
    serializer_class = ActionSerializer


# Roles and Permissions
class RolesPermissionsList(generics.ListCreateAPIView):
    """
    List all permissions associated with a role, or grant a new permission for a role.
    """
    queryset = Role_Permission.objects.all()
    serializer_class = RolePermissionSerializer

class RolePermissionsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a permission associated with a role.
    """
    queryset = Role_Permission.objects.all()
    serializer_class = RolePermissionSerializer


# User and Roles
class UserRolesList(generics.ListCreateAPIView):
    """
    List all roles associated with a user, or assign a new role for an user.
    """
    queryset = User_Roles.objects.all()
    serializer_class = UserRoleSerializer

class UserRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a role associated with an user.
    """
    queryset = User_Roles.objects.all()
    serializer_class = UserRoleSerializer

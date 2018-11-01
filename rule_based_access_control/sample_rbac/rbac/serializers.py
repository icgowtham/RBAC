from rest_framework import routers, serializers, viewsets

from rbac.models import Users, Roles, Resources, Actions, Role_Permission, User_Roles

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user', 'user_name')

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roles
        fields = ('role', 'role_name')

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resources
        fields = ('resource', 'resource_name')

class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actions
        fields = ('action', 'action_name')

class RolePermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role_Permission
        fields = ('role', 'resource', 'action')

class UserRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Roles
        fields = ('user', 'role')

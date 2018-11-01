from django.conf.urls import patterns, include, url
from django.contrib import admin
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

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resources.objects.all()
    serializer_class = ResourceSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionSerializer

class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = Role_Permission.objects.all()
    serializer_class = RolePermissionSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = User_Roles.objects.all()
    serializer_class = UserRoleSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users_management', UserViewSet)
router.register(r'roles_management', RoleViewSet)
router.register(r'resource_management', ResourceViewSet)
router.register(r'actions_management', ActionViewSet)
router.register(r'role_permission_management', RolePermissionViewSet)
router.register(r'user_role_management', UserRoleViewSet)


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rbac/', include('rbac.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
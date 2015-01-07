from django.contrib import admin
from rbac.models import Users, Roles, Actions, Resources, Role_Permission, User_Roles

# Register your models here.
class RolePermissionAdmin(admin.ModelAdmin):
	fields = ['role', 'resource', 'action']
	#list_display = ('role.role_name', 'role.resource_name', 'role.action_name')

class UserRoleAdmin(admin.ModelAdmin):
	fields = ['user', 'role']

admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(Actions)
admin.site.register(Resources)
admin.site.register(Role_Permission, RolePermissionAdmin)
admin.site.register(User_Roles)

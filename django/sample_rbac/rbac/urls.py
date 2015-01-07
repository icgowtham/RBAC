from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from rbac import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.UsersList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),    
    url(r'^roles/$', views.RolesList.as_view()),
    url(r'^roles/(?P<pk>[0-9]+)/$', views.RoleDetail.as_view()),    
    url(r'^resources/$', views.ResourcesList.as_view()),
    url(r'^resources/(?P<pk>[0-9]+)/$', views.ResourceDetail.as_view()),    
    url(r'^actions/$', views.ActionsList.as_view()),
    url(r'^actions/(?P<pk>[0-9]+)/$', views.ActionDetail.as_view()),    
    url(r'^role_permissions/$', views.RolesPermissionsList.as_view()),
    url(r'^role_permissions/(?P<pk>[0-9]+)/$', views.RolePermissionsDetail.as_view()),    
    url(r'^user_roles/$', views.UserRolesList.as_view()),
    url(r'^user_roles/(?P<pk>[0-9]+)/$', views.UserRoleDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
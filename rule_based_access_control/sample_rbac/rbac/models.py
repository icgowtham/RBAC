from django.db import models

# Create your models here.
class Users(models.Model):
        user = models.AutoField(primary_key=True)
        user_name = models.CharField(unique=True, max_length=200)
        
        def __str__(self):
        	return str(self.user) + " -> " + self.user_name
        
        class Meta:
        	ordering = ('user',)
        	verbose_name = 'Users'
        	verbose_name_plural = 'Users'


class Roles(models.Model):
        role = models.AutoField(primary_key=True)
        role_name = models.CharField(unique=True, max_length=200)

        def __str__(self):
        	return str(self.role) + " -> " + self.role_name

        class Meta:
        	ordering = ('role',)
        	verbose_name = 'Roles'
        	verbose_name_plural = 'Roles'


class Resources(models.Model):
        resource = models.AutoField(primary_key=True)
        resource_name = models.CharField(unique=True, max_length=200)

        def __str__(self):
        	return str(self.resource) + " -> " + self.resource_name

        class Meta:
        	ordering = ('resource',)
        	verbose_name = 'Resources'
        	verbose_name_plural = 'Resources'


class Actions(models.Model):
        action = models.AutoField(primary_key=True)
        action_name = models.CharField(unique=True, max_length=200)

        def __str__(self):
        	return str(self.action) + " -> " + self.action_name

        class Meta:
        	ordering = ('action',)
        	verbose_name = 'Actions'
        	verbose_name_plural = 'Actions'


class Role_Permission(models.Model):
        role = models.ForeignKey(Roles)
        resource = models.ForeignKey(Resources)
        action = models.ForeignKey(Actions)

        def __str__(self):
            return self.role.role_name + "--" + self.resource.resource_name + "--" + self.action.action_name

        class Meta:
            unique_together = ('role', 'resource', 'action',)
            ordering = ('role', 'resource', 'action',)
            verbose_name = 'Role_Permission'
            verbose_name_plural = 'Role_Permissions'


class User_Roles(models.Model):
        user = models.ForeignKey(Users)
        role = models.ForeignKey(Roles)

        def __str__(self):
            return self.user.user_name + "--" + self.role.role_name

        class Meta:
            unique_together = ('user', 'role',)
            ordering = ('user', 'role',)
            verbose_name = 'User_Roles'
            verbose_name_plural = 'User_Roles'

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')        
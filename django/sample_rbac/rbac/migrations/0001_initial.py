# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('action', models.AutoField(primary_key=True, serialize=False)),
                ('action_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Actions',
                'ordering': ('action',),
                'verbose_name': 'Actions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('resource', models.AutoField(primary_key=True, serialize=False)),
                ('resource_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Resources',
                'ordering': ('resource',),
                'verbose_name': 'Resources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role_Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(to='rbac.Actions')),
                ('resource', models.ForeignKey(to='rbac.Resources')),
            ],
            options={
                'verbose_name_plural': 'Role_Permissions',
                'ordering': ('role', 'resource', 'action'),
                'verbose_name': 'Role_Permission',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Roles',
                'ordering': ('role',),
                'verbose_name': 'Roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(to='rbac.Roles')),
            ],
            options={
                'verbose_name_plural': 'User_Roles',
                'ordering': ('user', 'role'),
                'verbose_name': 'User_Roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ('user',),
                'verbose_name': 'Users',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user_roles',
            name='user',
            field=models.ForeignKey(to='rbac.Users'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='user_roles',
            unique_together=set([('user', 'role')]),
        ),
        migrations.AddField(
            model_name='role_permission',
            name='role',
            field=models.ForeignKey(to='rbac.Roles'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='role_permission',
            unique_together=set([('role', 'resource', 'action')]),
        ),
    ]

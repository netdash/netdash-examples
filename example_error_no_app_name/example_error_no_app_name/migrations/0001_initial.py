# Generated by Django 2.2.2 on 2019-07-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModulePermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': [('can_view_module', 'Can see link in the NetDash navbar and access module.')],
                'managed': False,
                'default_permissions': [],
            },
        ),
    ]

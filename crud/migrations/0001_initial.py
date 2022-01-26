# Generated by Django 4.0.1 on 2022-01-26 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.generic.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('iban', localflavor.generic.models.IBANField(include_countries=None, max_length=34, use_nordea_extensions=False, verbose_name='IBAN')),
                ('cuser', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CUSER', to=settings.AUTH_USER_MODEL, verbose_name='Administrator')),
            ],
            options={
                'verbose_name': 'User Data',
                'verbose_name_plural': 'User Data',
            },
        ),
    ]

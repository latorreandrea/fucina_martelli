# Generated by Django 3.2 on 2022-03-15 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email_address', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('street_address1', models.CharField(blank=True, max_length=40, null=True)),
                ('street_address2', models.CharField(blank=True, max_length=40, null=True)),
                ('county', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.2 on 2022-02-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220224_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(choices=[('steel', 'steel'), ('titanium', 'titanium')], default=0, max_length=100),
        ),
    ]

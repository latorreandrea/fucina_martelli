# Generated by Django 3.2 on 2022-02-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(choices=[('0', 'no'), ('10', '10% discount'), ('20', '20% discount')], default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.CharField(choices=[('0', 'no'), ('10', '10% discount'), ('20', '20% discount')], default=1, max_length=100),
        ),
    ]

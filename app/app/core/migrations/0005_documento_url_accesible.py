# Generated by Django 4.1.4 on 2023-01-26 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_documento_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='url_accesible',
            field=models.CharField(default='', max_length=100),
        ),
    ]
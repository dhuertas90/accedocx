# Generated by Django 4.1.4 on 2023-01-02 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='pdf',
            new_name='doc',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='cover',
            new_name='portada',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='titulo',
        ),
    ]

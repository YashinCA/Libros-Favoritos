# Generated by Django 4.0.2 on 2022-03-03 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='descripcion',
            new_name='description',
        ),
    ]
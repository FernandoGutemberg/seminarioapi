# Generated by Django 4.1.2 on 2022-12-07 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='id_cliente',
            new_name='id_clientes',
        ),
    ]

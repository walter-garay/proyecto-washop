# Generated by Django 4.2.5 on 2023-11-08 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_imagen_inventario_remove_opcionvariante_variante_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre_categoria',
            new_name='nombre',
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-08 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_cliente_departamento_distrito_estadoventa_garantia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(blank=True, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='opcionvariante',
            name='variante',
        ),
        migrations.RemoveField(
            model_name='variante',
            name='producto',
        ),
        migrations.RenameField(
            model_name='negocio',
            old_name='fb',
            new_name='fb_url',
        ),
        migrations.RenameField(
            model_name='negocio',
            old_name='ig',
            new_name='ig_url',
        ),
        migrations.RenameField(
            model_name='negocio',
            old_name='nombre_negocio',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='negocio',
            old_name='tiktok',
            new_name='tiktok_url',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_producto',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='negocio',
            name='rubro',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.AddField(
            model_name='negocio',
            name='logo_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='negocio',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.pais'),
        ),
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('imagen_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.imagen')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.producto')),
            ],
            bases=('ecommerce.imagen',),
        ),
        migrations.DeleteModel(
            name='Garantia',
        ),
        migrations.DeleteModel(
            name='OpcionVariante',
        ),
        migrations.DeleteModel(
            name='UnidadTiempo',
        ),
        migrations.DeleteModel(
            name='Variante',
        ),
        migrations.AddField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.producto'),
        ),
    ]

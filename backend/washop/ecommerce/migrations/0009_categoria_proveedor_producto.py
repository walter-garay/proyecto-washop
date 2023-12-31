# Generated by Django 4.2.5 on 2023-09-28 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_negocio_rol_rubro_usuarionegocio_negocio_rubro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.EmailField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('nombre_producto', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.categoria')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.proveedor')),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-03 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField(default=0)),
                ('stock', models.FloatField(default=0)),
                ('iva', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos_orm.Cliente')),
            ],
            options={
                'verbose_name': 'factura',
                'verbose_name_plural': 'facturas',
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('subtotal', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos_orm.Factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelos_orm.Producto')),
            ],
            options={
                'verbose_name': 'detalle',
                'verbose_name_plural': 'detalles',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='producto',
            field=models.ManyToManyField(to='modelos_orm.Producto'),
        ),
    ]
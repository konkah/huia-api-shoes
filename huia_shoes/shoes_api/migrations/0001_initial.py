# Generated by Django 3.2.5 on 2021-07-10 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier_code', models.CharField(max_length=100)),
                ('manufacturing_date', models.DateField()),
                ('product_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier_code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('colour', models.CharField(choices=[('red', 'Vermelho'), ('blue', 'Azul'), ('green', 'Verde'), ('yellow', 'Amarelo'), ('orange', 'Laranja'), ('purple', 'Roxo')], default='blue', max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('value', models.FloatField()),
                ('batch_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shoes_api.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('seller', models.CharField(max_length=50)),
                ('total_value', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shoes_api.client')),
                ('products', models.ManyToManyField(to='shoes_api.Product')),
            ],
        ),
    ]

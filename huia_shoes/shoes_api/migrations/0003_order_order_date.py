# Generated by Django 3.2.5 on 2021-07-10 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_api', '0002_alter_client_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date(2021, 7, 10)),
            preserve_default=False,
        ),
    ]

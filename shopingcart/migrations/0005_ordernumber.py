# Generated by Django 2.0.6 on 2018-12-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopingcart', '0004_shippingaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.IntegerField(default=170)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='country',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='email',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='name',
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='shippingaddress',
            table=None,
        ),
        migrations.DeleteModel(
            name='ShippingAddress2',
        ),
    ]

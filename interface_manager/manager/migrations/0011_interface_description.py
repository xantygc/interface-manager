# Generated by Django 3.2.20 on 2023-07-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_alter_interface_business_process'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]

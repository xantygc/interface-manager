# Generated by Django 3.2.20 on 2023-07-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_system_is_monitoring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='deprecation_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='interface',
            name='production_date',
            field=models.DateField(default=None, null=True),
        ),
    ]

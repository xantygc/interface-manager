# Generated by Django 3.2.20 on 2023-07-17 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_interface_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endpoint',
            name='system',
        ),
        migrations.AddField(
            model_name='system',
            name='endpoints',
            field=models.ManyToManyField(to='manager.Endpoint'),
        ),
    ]

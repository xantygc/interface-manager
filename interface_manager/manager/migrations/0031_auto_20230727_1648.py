# Generated by Django 3.2.20 on 2023-07-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0030_interface_tech'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interface',
            name='tech',
        ),
        migrations.AddField(
            model_name='interface',
            name='technology',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

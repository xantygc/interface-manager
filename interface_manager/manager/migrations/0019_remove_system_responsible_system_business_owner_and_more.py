# Generated by Django 4.2.3 on 2023-07-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0018_remove_system_endpoints_delete_endpoint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='responsible',
        ),
        migrations.AddField(
            model_name='system',
            name='business_owner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='system',
            name='it_owner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

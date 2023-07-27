# Generated by Django 3.2.20 on 2023-07-27 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0027_auto_20230727_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='interface',
            name='endpoint',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interface',
            name='technology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.technology'),
        ),
    ]
# Generated by Django 3.2.20 on 2023-07-16 17:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('responsible', models.CharField(max_length=200)),
                ('is_monitoring', models.BooleanField(default=False)),
                ('monitoring URL', models.URLField(blank=True, default=None)),
                ('is_alarmed', models.BooleanField(default=False)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('production_ready', models.DateField(default=None, null=True)),
                ('deprecation_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.IntegerField(choices=[(0, 'Wsdl'), (1, 'Rest API'), (2, 'sFTP'), (3, 'FTP'), (4, 'ESB Integration')], default=None)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('production_date', models.DateField(blank=True, default=None)),
                ('deprecation_date', models.DateField(blank=True, default=None)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination', to='manager.system')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='source', to='manager.system')),
            ],
        ),
    ]

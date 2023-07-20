import django
from django.db import models
from django.utils.translation import gettext_lazy as _


class System(models.Model):
    name = models.CharField(name='name', max_length=100)
    responsible = models.CharField(max_length=200)
    technology = models.CharField(name='technology', max_length=150, blank=True, null=True)
    monitoring = models.BooleanField(name='is_monitoring', default=False)
    monitoring_url = models.URLField(name='monitoring URL', null=True, blank=True, default=None)
    alarms = models.BooleanField(name='is_alarmed', default=False)
    external = models.BooleanField(name='is_external', default=False)
    creation_date = models.DateField(name='creation_date', default=django.utils.timezone.now)
    production_ready = models.DateField(name='production_ready', null=True, blank=True, default=None)
    deprecation_date = models.DateField(name='deprecation_date', null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class BusinessProcess(models.Model):
    class Unit(models.IntegerChoices):
        COME_ES = 0, _('COME ES')
        COME_PT = 1, _('COME PT')
        GAS_TOP = 2, _('GAS TOP')
        AGENTE_VENDEDOR = 3, _('AGENTE_VENDEDOR')

    unit = models.IntegerField(name='department', default=None, choices=Unit.choices)
    process = models.CharField(name='name', max_length=100)

    def __str__(self):
        return self.get_department_display() + ' - ' + self.name

class Interface(models.Model):
    class Technology(models.IntegerChoices):
        WSDL = 0, _('Wsdl')
        REST_API = 1, _('Rest API')
        SFTP = 2, _('sFTP')
        FTP = 3, _('FTP')
        ESB = 4, _('ESB Integration')

    process = models.ForeignKey(BusinessProcess, on_delete=models.DO_NOTHING, name="business_process")
    source = models.ForeignKey(System, on_delete=models.DO_NOTHING, name="source", related_name="source")
    destination = models.ForeignKey(System, on_delete=models.DO_NOTHING, name="destination", related_name="destination")
    technology = models.IntegerField(default=None, choices=Technology.choices)
    description = models.CharField(max_length=50, null=True, blank=True, name="description")
    alarms = models.BooleanField(name='is_alarmed', default=False)
    monitoring = models.BooleanField(name='is_monitoring', default=False)
    monitoring_url = models.URLField(name='monitoring URL', null=True, blank=True, default=None)
    creation_date = models.DateField(name='creation_date', default=django.utils.timezone.now)
    production_ready = models.DateField(name='production_date', blank=True, null=True, default=None)
    deprecation_date = models.DateField(name='deprecation_date', blank=True, null=True, default=None)

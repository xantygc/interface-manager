import django
from django.db import models
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(max_length=50)
    it_owner = models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, null=True)
    technology = models.CharField(name='technology', max_length=150, blank=True, null=True)
    infra_monitoring = models.BooleanField(name='infrastructure_monitoring', default=False)
    app_monitoring = models.BooleanField(name='app_monitoring', default=False)
    business_monitoring = models.BooleanField(name='business_monitoring', default=False)
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
    process = models.CharField(name='name', max_length=100)
    business_area = models.ForeignKey(Department, name='business_area', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.business_area)    + ' - ' + self.name

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

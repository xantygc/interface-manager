import django
from django.db import models
from django.utils.translation import gettext_lazy as _


class Technology(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


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
    process_url = models.URLField(name="url", null=True, blank=True)

    def __str__(self):
        return str(self.business_area) + ' - ' + self.name


class Interface(models.Model):
    process = models.ForeignKey(BusinessProcess, on_delete=models.DO_NOTHING, name="business_process")
    source = models.ForeignKey(System, on_delete=models.PROTECT, name="source", related_name='source')
    destination = models.ForeignKey(System, on_delete=models.PROTECT, name="destination", related_name='destination')
    endpoint = models.URLField(null=True, blank=True)
    technology = models.ForeignKey(Technology, on_delete=models.PROTECT, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True, name="description")
    alarms = models.BooleanField(name='is_alarmed', default=False)
    monitoring = models.BooleanField(name='is_monitoring', default=False)
    creation_date = models.DateField(name='creation_date', default=django.utils.timezone.now)
    production_ready = models.DateField(name='production_date', blank=True, null=True, default=None)
    deprecation_date = models.DateField(name='deprecation_date', blank=True, null=True, default=None)

from django.contrib import admin
from .models import Interface, System, BusinessProcess, Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "it_owner"]

class SystemAdmin(admin.ModelAdmin):
    list_display = ["name", "technology", "is_alarmed", "is_monitoring", "production_ready"]

class InterfaceAdmin(admin.ModelAdmin):
    list_display = ["get_business_process_dpto", "get_business_process_name", "get_source_name", "get_destination_name"]

    def get_business_process_dpto(self, obj):
        return obj.business_process.business_area.name

    def get_business_process_name(self, obj):
        return obj.business_process.name

    def get_source_name(self, obj):
        return obj.source.name

    def get_destination_name(self, obj):
        return obj.destination.name

class BusinessProcessAdmin(admin.ModelAdmin):
    list_display = ["business_area", "name"]

admin.site.register(System, SystemAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(BusinessProcess, BusinessProcessAdmin)
admin.site.register(Department, DepartmentAdmin)

from django.contrib import admin
from .models import Interface, System, BusinessProcess, Department, Technology

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "it_owner"]

class SystemAdmin(admin.ModelAdmin):
    list_display = ["name", "is_external", "description", "is_alarmed", "is_monitoring", "production_ready"]

class InterfaceAdmin(admin.ModelAdmin):
    
    list_display = ["id","get_source_name", "get_destination_name", "get_business_process_dpto", "get_business_process_name",  "is_alarmed", "is_monitoring"]

    def get_business_process_dpto(self, obj):
        return obj.business_process.business_area.name

    def get_business_process_name(self, obj):
        return obj.business_process.name

    def get_source_name(self, obj):
        return obj.source.name

    def get_destination_name(self, obj):
        return obj.destination.name

class BusinessProcessAdmin(admin.ModelAdmin):
    list_display = ["business_area", "name", "url"]

admin.site.register(Technology)
admin.site.register(System, SystemAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(BusinessProcess, BusinessProcessAdmin)
admin.site.register(Department, DepartmentAdmin)

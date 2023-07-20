from django.contrib import admin
from .models import Interface, System, BusinessProcess



class SystemAdmin(admin.ModelAdmin):
    fields = ["name", "responsible", "technology", "is_monitoring", "monitoring URL", "is_alarmed", "is_external", "production_ready", "deprecation_date"]
    list_display = ["name", "responsible", "technology", "production_ready"]

class InterfaceAdmin(admin.ModelAdmin):
    list_display = ["get_business_process_dpto", "get_business_process_name", "get_source_name", "get_destination_name"]



    def get_business_process_dpto(self, obj):
        return obj.business_process.get_department_display()


    def get_business_process_name(self, obj):
        return obj.business_process.name

    def get_source_name(self, obj):
        return obj.source.name

    def get_destination_name(self, obj):
        return obj.destination.name

class BusinessProcessAdmin(admin.ModelAdmin):
    list_display = ["department", "name"]


admin.site.register(System, SystemAdmin)
admin.site.register(Interface, InterfaceAdmin)
admin.site.register(BusinessProcess, BusinessProcessAdmin)



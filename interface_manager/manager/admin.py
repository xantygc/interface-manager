from django.contrib import admin
from django.utils.html import format_html

from .models import Interface, System, BusinessProcess, Department, Technology

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ["name", "it_owner", "diagram_url"]
	def diagram_url(self, obj):
		return format_html('<a target="_blank" href="/manager/diagram_area/{0}" >Generate diagram</a>&nbsp;', str(obj.id))
	diagram_url.allow_tags = True
	diagram_url.short_description = 'Actions'


class SystemAdmin(admin.ModelAdmin):
	list_per_page = 15
	search_fields = ["name"]
	list_filter = ["is_external"]
	list_display = ["name", "is_external", "description", "is_alarmed", "is_monitoring", "production_ready", "diagram_url"]
	ordering = ["name"]
	def diagram_url(self, obj):
		return format_html('<a target="_blank" href="/manager/diagram_system/{0}" >Generate diagram</a>&nbsp;', str(obj.id))
	diagram_url.allow_tags = True
	diagram_url.short_description = 'Actions'

class InterfaceAdmin(admin.ModelAdmin):
	search_fields = ["source__name","destination__name"]
	list_per_page = 15
	ordering = ["source__name", "destination__name"]
	list_filter = ['technology', 'business_process']
	list_display = ["id", "get_source_name", "get_destination_name", "get_business_process_dpto",
					"get_business_process_name", "technology", "endpoint", "is_alarmed", "is_monitoring"]

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

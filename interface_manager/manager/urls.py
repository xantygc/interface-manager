from django.urls import path
from . import views

urlpatterns=[
		path("", views.index, name="index"),
		path("system/", views.system, name="system"),
		path("interface/", views.interface, name="interface"),
		path("system/<id>", views.system_detail, name="system_detail"),
		path("interface/<id>", views.interface_detail, name="interface_detail"),
		path("endpoint/<id>", views.endpoint_detail, name="endpoint_detail"),

	]
import os
from tempfile import NamedTemporaryFile

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .diagram import create_diagram
from .models import System, Interface, Department


def index(request):
	existing_systems_list = System.objects.all().order_by('name').values()
	context = {"system_list": existing_systems_list}
	return render(request, "manager/index.html", context)


def system(request):
	existing_systems_list = System.objects.all().order_by('name').values()
	context = {"system_list": existing_systems_list}
	return render(request, "manager/system.html", context)


def system_detail(request):
	context = {}
	return render(request, "manager/system/detail.html", context)


def interface(request):
	existing_interfaces_list = Interface.objects.all()
	context = {"interface_list": existing_interfaces_list}
	return render(request, "manager/interface.html", context)


def interface_detail(request):
	context = {}
	return render(request, "manager/system/detail.html", context)


def endpoint_detail(request):
	context = {}
	return render(request, "manager/endpoint/detail.html", context)


def diagram_business_area(request, id):
	area = Department.objects.get(id=id)
	interfaces_area = Interface.objects.filter(business_process__business_area__id=id)
	filename = NamedTemporaryFile(dir="./").name
	create_diagram(filename, interfaces=interfaces_area)
	with open(filename + ".png", "rb") as f:
		diagram_data = f.read()

	return HttpResponse(diagram_data, content_type="image/png")


def diagram_system(request, id):
	system = System.objects.get(id=id)
	interfaces = Interface.objects.filter(Q(source=system) | Q(destination=system))

	filename = NamedTemporaryFile(dir="./").name
	create_diagram(filename, interfaces=interfaces)
	with open(filename + ".png", "rb") as f:
		diagram_data = f.read()
	return HttpResponse(diagram_data, content_type="image/png")


def delete_file(filename):
	if os.path.exists(filename):
		# Intentamos eliminar el archivo
		try:
			os.remove(filename)
			print("Archivo borrado exitosamente.")
		except OSError as e:
			print(f"No se pudo borrar el archivo: {e}")
	else:
		print("El archivo no existe.")

from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from diagrams import Diagram, Cluster
from diagrams.c4 import System, Relationship
from .models import System, Interface, BusinessProcess
from diagrams import Diagram
from diagrams.generic.os import Windows
from diagrams.generic.database import SQL
from diagrams.generic.blank import Blank

# Create your views here.

def index(request):
	existing_systems_list = System.objects.all()
	context = {"system_list": existing_systems_list}
	return render(request, "manager/index.html", context)

def system(request):
	existing_systems_list = System.objects.all()
	context = {"system_list": existing_systems_list}
	return render(request, "manager/system.html", context)

def system_detail(request):
	context = {}
	return render(request, "manager/system/detail.html",context)

def interface(request):
	existing_interfaces_list = Interface.objects.all()
	context = {"interface_list": existing_interfaces_list}
	return render(request, "manager/interface.html", context)

def interface_detail(request):
	context = {}
	return render(request, "manager/system/detail.html",context)

def endpoint_detail(request):
	context = {}
	return render(request, "manager/endpoint/detail.html",context)

def diagram_view(request, id):
	try:
		interfaces = Interface.objects.filter(business_process__id=1)
	except Interface.DoesNotExist:
		interfaces = None

	try:
		bp = BusinessProcess.objects.get(id=id)
		unit_display = bp.department
	except BusinessProcess.DoesNotExist:
		# maneja el caso en que no existe un BusinessProcess con ese id
		unit_display = None
	print(bp)

	diag_path="pepe"

	with Diagram("My Diagram", show=False, filename=diag_path):
		for i in interfaces:
			source_system = i.source
			destination_system = i.destination

			with Diagram("My Diagram", show=False, filename=diag_path):
				source = System(source_system.name)
				destination = System(destination_system.name)
				source >> destination

	response = FileResponse(open("pepe.png", 'rb'))
	return response
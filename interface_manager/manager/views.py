from django.http import HttpResponse
from django.shortcuts import render

from .models import System, Interface


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
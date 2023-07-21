from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
def root_redirect(request):
    return redirect('system')


urlpatterns = [
    path('', root_redirect, name='root_redirect'),
    path("admin/", admin.site.urls),
    path("manager/", include('manager.urls'))
]
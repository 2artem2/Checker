from django.shortcuts import render
from django.http import HttpResponse
from .models import Site



def index(request):
    site_list = Site.objects.order_by("created_at")[:]
    output = "  "
    for q in site_list:
        output += (q.name) + ":"
        output += (str(q.port_site)) + " "
    
    return HttpResponse(output)
# Create your views here.

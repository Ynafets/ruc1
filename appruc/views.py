from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    # create a dictionary to pass
    # data to the template
    data={}
    if 'rucname' in request.GET:
        rucname=request.GET['rucname']

        url='https://api.apis.net.pe/v1/ruc?numero=%s' % rucname
        data=requests.get(url)
        data= data.json()

    
    # return response with template and context
    return render(request, "ruc.html",data)
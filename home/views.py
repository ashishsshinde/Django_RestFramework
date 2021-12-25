from django.http.response import HttpResponse
from django.shortcuts import render
from home.serializers import Visitserializer
from home.models import Visit
from rest_framework.renderers import JSONRenderer


# Create your views here.


def index(request):   
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        noofguest = request.POST.get('noofguest')
        typeofacc = request.POST.get('typeofacc')
        # return HttpResponse(fromdate)
        Visit111 = Visit(fromdate=fromdate, todate=todate,
                         noofguest=noofguest, typeofacc=typeofacc)
        Visit111.save()

    data = {
        "title": "Home",
        "description": "BAAP AGRO"
    }
    return render(request, 'index.html', data)


def contact(request):    
    return render(request, 'contact.html')

def visit_details(request):
    visit_details = Visit.object.get(id=1)
    serializer_data = Visitserializer(visit_details)
    json_data = JSONRenderer().render(serializer_data)
    return HttpResponse(json_data)
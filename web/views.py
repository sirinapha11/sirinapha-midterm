from django.shortcuts import render
from web.models import Hospital

# Create your views here.
def index(request):
    context = {}
    context ['hospital'] = Hospital.objects.all()
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')

def hospi(request):
    return render(request, 'hospi.html')

def user(request):
    return render(request, 'user.html')

def detall(request, id):
    context = {}
    hospitals = Hospital.objects.filter(id=id)
    for hospital in hospitals :
        context['hospital'] = hospital
    return render(request, "detall.html", context)


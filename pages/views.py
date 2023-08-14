from django.shortcuts import render
from django.http import HttpResponse
from corse.models import Lectuer
from corse.models import Corses

# Create your views here.
def index (request):
    context={
        'lectuers':Lectuer.objects.all(),
        'corses':Corses.objects.all()
    }
    return render(request, 'pges/index.html',context)
def about (request):
    return render(request, 'pges/about.html')
def privacy (request):
    return render(request, 'pges/privacy_policy.html')

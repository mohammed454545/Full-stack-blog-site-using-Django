from django.shortcuts import render,get_object_or_404
from .models import Lectuer
from .models import Corses

# Create your views here.
def corse (request,cor_id):
    lecrs=Lectuer.objects.all()
    lecrs=lecrs.filter(cors_name__icontains=cor_id)
    context={
        'lectuers':lecrs,
    }
    return render(request, 'pges/corse.html',context)
def allcorses (request):
    name=None
    corss=Corses.objects.all()
    if 'searchname' in  request.GET:
        name=request.GET['searchname']
        if name:
            corss=corss.filter(title__icontains=name)
    context={
        'corses':corss
    }
    return render(request, 'pges/allcorses.html',context)
def lectuer (request,lec_id):
    context={
        'lec':get_object_or_404(Lectuer,pk=lec_id)
    }
    return render(request, 'pges/lectuer.html', context)

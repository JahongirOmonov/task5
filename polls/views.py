
from django.shortcuts import render
from .models import maktab, xonalar
from django.http import JsonResponse

# Create your views here.

def all(request):
    obshi=maktab.objects.all()
    allitem =[]
    for i in obshi:
        allitem.append({
            'name':i.name,
            'oquvchilar_soni':i.oquvchilar_soni
        })
    return JsonResponse(allitem, safe=False)
    


def detail(request, shuid):
    each = xonalar.objects.get(id=shuid)
    data={'Xona nomi':each.xonanomi, 'nechi kishiligi':each.nechikishiligi}
    return JsonResponse(data, safe=False)
        

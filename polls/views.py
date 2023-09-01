
from django.shortcuts import render
from .models import maktab, xonalar
from django.http import JsonResponse
from .serializer import maktabSerializer, xonalarSerializer

# Create your views here.

def all(request):
    all=maktab.objects.all()
    result=maktabSerializer(all, many=True)
    # for i in obshi:
    #     allitem.append({
    #         'name':i.name,
    #         'oquvchilar_soni':i.oquvchilar_soni
    #     })
    return JsonResponse(result.data, safe=False)
    


def detail(request, shuid):
    some = xonalar.objects.filter(id=myid)
    forgett = xonalarSerializer(some, many=True)
    return JsonResponse(forgett, safe=False)
        

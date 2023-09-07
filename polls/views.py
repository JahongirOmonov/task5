
from django.shortcuts import render
from .models import maktab, xonalar
from django.http import JsonResponse
from .serializer import maktabSerializer, xonalarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def all(request):
#     all=maktab.objects.all()
#     result=maktabSerializer(all, many=True)
#     # for i in obshi:
#     #     allitem.append({
#     #         'name':i.name,
#     #         'oquvchilar_soni':i.oquvchilar_soni
#     #     })
#     return JsonResponse(result.data, safe=False)

class getmaktab(APIView):
    def get(self, request):
        good = maktab.objects.all()
        serkalaz=maktabSerializer(good, many=True)
        return Response(serkalaz.data)
    


def detail(request, shuid):
    some = xonalar.objects.filter(id=myid)
    forgett = xonalarSerializer(some, many=True)
    return JsonResponse(forgett, safe=False)

class psotmaktab(APIView):
    def post(self, request):
        asosiy_qism=request.data
        serialize = fullnameSerializer(data=asosiy_qism)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)
        

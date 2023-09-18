
from django.shortcuts import render
from .models import maktab, xonalar
from django.http import JsonResponse
from .serializer import maktabSerializer, xonalarSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

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

# class getmaktab(APIView):
#     def get(self, request):
#         good = maktab.objects.all()
#         serkalaz=maktabSerializer(good, many=True)
#         return Response(serkalaz.data)
class GetAllMaktab(generics.ListAPIView):
    queryset=maktab.objects.all()
    serializer_class=maktabSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return maktab.objects.all()

class GetDetailMaktab(generics.RetrieveAPIView):
    queryset = maktab.objects.all()
    serializer_class=maktabSerializer

class PostMaktab(generics.CreateAPIView):
    queryset=maktab.objects.all()
    serializer_class=maktabSerializer

    

class PatchMaktab(generics.UpdateAPIView):
    queryset=maktab.objects.all()
    serializer_class=maktabSerializer
# class getmaktab(APIView):
#     def get(self, request):
#         good = maktab.objects.all()
#         serkalaz=maktabSerializer(good, many=True)
#         return Response(serkalaz.data)


class DeleteMaktab(generics.DestroyAPIView):
    queryset=maktab.objects.all()
    serializer_class=maktabSerializer

class PostGetMaktab(generics.ListCreateAPIView):
    queryset=maktab.objects.all()
    serializer_class=maktabSerializer

class AllFunctionMaktab(generics.RetrieveUpdateDestroyAPIView):
    queryset=maktab.objects.all()
    serializer_class=maktabSerializer


    


# def detail(request, shuid):
#     some = xonalar.objects.filter(id=myid)
#     forgett = xonalarSerializer(some, many=True)
#     return JsonResponse(forgett, safe=False)

# class psotmaktab(APIView):
#     def post(self, request):
#         asosiy_qism=request.data
#         serialize = fullnameSerializer(data=asosiy_qism)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data)
#         return Response(serialize.errors)

class GetAllXonalar(generics.ListAPIView):
    queryset=xonalar.objects.all()
    serializer_class=xonalarSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return xonalar.objects.all()

class GetDetailXonalar(generics.RetrieveAPIView):
    queryset = xonalar.objects.all()
    serializer_class=xonalarSerializer






class PostXonalar(generics.CreateAPIView):
    queryset=xonalar.objects.all()
    serializer_class=xonalarSerializer





# class psotmaktab(APIView):
#     def post(self, request):
#         asosiy_qism=request.data
#         serialize = fullnameSerializer(data=asosiy_qism)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data)
#         return Response(serialize.errors)







class PatchXonalar(generics.UpdateAPIView):
    queryset=xonalar.objects.all()
    serializer_class=xonalarSerializer

class DeleteXonalar(generics.DestroyAPIView):
    queryset=xonalar.objects.all()
    serializer_class=xonalarSerializer







class PostGetXonalar(generics.ListCreateAPIView):
    queryset=xonalar.objects.all()
    serializer_class=xonalarSerializer

class AllFunctionXonalar(generics.RetrieveUpdateDestroyAPIView):
    queryset=xonalar.objects.all()
    serializer_class=xonalarSerializer
        

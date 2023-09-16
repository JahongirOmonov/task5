from django.urls import path
from .views import (GetAllXonalar, GetDetailXonalar, 
                    PostXonalar, PatchXonalar, DeleteXonalar,
                      AllFunctionXonalar,
                        PostGetXonalar)


from .views import GetAllMaktab, PostMaktab, GetDetailMaktab, PatchMaktab, DeleteMaktab, AllFunctionMaktab, PostGetMaktab

urlpatterns=[
    path('GetAllMaktab/', GetAllMaktab.as_view()),
    
    path('GetDetailMaktab/<int:pk>', GetDetailMaktab.as_view()),
    path('PostMaktab/', PostMaktab.as_view() ),


    path('PatchMaktab/<int:pk>', PatchMaktab.as_view()),


    path('DeleteMaktab/<int:pk>', DeleteMaktab.as_view()),
    path('PostGetMaktab/', PostGetMaktab.as_view()),
    path('AllFunctionMaktab/<int:pk>', AllFunctionMaktab.as_view()),


    path('GetAllXonalar/', GetAllXonalar.as_view()),

    path('GetDetailXonalar/<int:pk>', GetDetailXonalar.as_view())
    
    ,
    path('PostXonalar/', PostXonalar.as_view() ),
    path('PatchXonalar/<int:pk>', PatchXonalar.as_view()),

    path('DeleteXonalar/<int:pk>', DeleteXonalar.as_view()),


    path('PostGetXonalar/', PostGetXonalar.as_view()),
    path('AllFunctionXonalar/<int:pk>', AllFunctionXonalar.as_view())


]
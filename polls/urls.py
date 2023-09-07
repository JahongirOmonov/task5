from django.urls import path
from .views import getmaktab, psotmaktab, detail

urlpatterns=[
    path('all/', getmaktab.as_view()),
    path('detail/<int:shuid>', detail),
    path('create/>', psotmaktab.as_view())
]
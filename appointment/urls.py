from django.urls import path
from . import views

urlpatterns = [

    # path('',views.add ),
    path('insert',views.insert,name='insert'),
    # path('add',views.add,name='add'),


]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexView),
     path('contact',views.contact,name='contact'),
    # path('add',views.add,name='add'),


]

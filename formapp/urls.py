from django.urls import path


from . import views
app_name='formapp'


urlpatterns=[ 
    path('create/',views.Carview,name='create'),
    path('sample/',views.sample,name='sample'),
    path('readall/',views.readview,name='readall'),
    path('readone/<pk>/',views.readone,name='readone'),
    path('read/',views.read,name='read'),
    path('updateone/<pk>/',views.updateone,name='updateone'),
    path('updateread/',views.updateread,name='updateread'),
    path('delete/<pk>/',views.delete,name='delete'),
]

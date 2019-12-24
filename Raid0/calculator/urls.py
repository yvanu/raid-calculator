from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test',views.test,name='test'),
    #path('raid1',views.raid1,name='raid1'),
    #path('R5',views.R5,name='R5'),
    #path('R6',views.R6,name='R6'),
    #path('R10',views.R10,name='R10'),
]
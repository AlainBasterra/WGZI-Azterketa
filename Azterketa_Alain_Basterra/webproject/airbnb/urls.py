from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    #Orri nagusiak
    path('', views.index, name='index'),
    path('etxeak', views.etxeak, name='etxeak'),
    path('pertsonak', views.pertsonak, name='pertsonak'),

    # Etxea crud
    path('formaddetxea/', views.formaddetxea, name='formaddetxea'),
    path('formaddetxea/addetxea/', views.addetxea, name='addetxea'),

    path('deleteetxea/<int:id>/', views.deleteetxea, name='deleteetxea'),

    path('formupdateetxea/<int:id>/', views.formupdateetxea, name='formupdateetxea'),
    path('formupdateetxea/updateetxea/', views.updateetxea, name='etxeak'),

    # Pertsona crud
    path('formaddpertsona/', views.formaddpertsona, name='formaddpertsona'),
    path('formaddpertsona/addpertsona/', views.addpertsona, name='addpertsona'),

    path('deletepertsona/<int:id>/', views.deletepertsona, name='deletepertsona'),

    path('formupdatepertsona/<int:id>/', views.formupdatepertsona, name='formupdatepertsona'),
    path('formupdatepertsona/updatepertsona/', views.updatepertsona, name='updatepertsona'),
]

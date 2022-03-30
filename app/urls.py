from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('career/', views.career, name="career"),
    path('apply/', views.apply, name='apply'),

]

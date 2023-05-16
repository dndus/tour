from django.urls import path
from .views import *

urlpatterns = [
    path('', main_index, name='index'),
    path('about/', main_about, name='about'),
    path('services/', main_service, name='services'),
    path('contact/', main_contact, name='contact')
]
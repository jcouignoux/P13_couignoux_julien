
from django.urls import path

from oc_lettings_site import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
]

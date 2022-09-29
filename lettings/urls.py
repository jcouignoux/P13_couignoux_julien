from django.urls import path

from lettings import views

app_name = 'lettings'

urlpatterns = [
    path('', views.lettings_index, name="lettings_index"),
    path('<int:letting_id>/', views.letting, name='letting'),
]

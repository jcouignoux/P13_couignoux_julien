from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include(('website.urls', 'website'), namespace='website')),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
]

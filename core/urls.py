from django.urls import include, path
from .views import *

app_name ='core'

urlpatterns = [
    path('',home,name='home'),
    path('create-script',create_script,name='create_script'),
    path('about-us/',about,name='about'),
    path('pricing/',pricing,name='pricing'),
    path('for-studios/',for_studios,name='for_studios'),
    path('features/',features,name='features'),
    path('blog/',blog,name='blog'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]
from .views import ProfilesDetailView
from django.conf.urls import url, include


urlpatterns = [

    url(r'^(?P<username>[\w-]+)/$', ProfilesDetailView.as_view(), name= "detail"),

]
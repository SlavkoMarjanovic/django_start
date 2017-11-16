from .views import ProfilesDetailView
from django.conf.urls import url, include


urlpatterns = [
<<<<<<< HEAD
=======

>>>>>>> 2fce28706731f3181d1bc144b6311ae5cf875fa2
    url(r'^(?P<username>[\w-]+)/$', ProfilesDetailView.as_view(), name= "detail"),

]
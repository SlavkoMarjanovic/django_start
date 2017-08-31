from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

user = get_user_model()
class ProfilesDetailView(DetailView):
    queryset = user.objects.filter(is_active =True)


# Create your views here.

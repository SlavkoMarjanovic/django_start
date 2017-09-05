from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import Http404
from django.contrib.auth import get_user_model

User = get_user_model()
class ProfilesDetailView(DetailView):

    template_name = 'profiles/user.html'

    def get_object(self):
        user_name = self.kwargs.get("username")
        if user_name is None:
            raise Http404
        return get_object_or_404(User, username__iexact=user_name, is_active =True)


# Create your views here.

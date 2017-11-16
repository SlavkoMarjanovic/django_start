from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.http import Http404
from django.contrib.auth import get_user_model
from restaurant.models import RestaurantLocation

User = get_user_model()
class ProfilesDetailView(DetailView):
    template_name = 'profiles/user.html'
    def get_object(self):
        user_name = self.kwargs.get("username")
        if user_name is None:
            raise Http404
        return get_object_or_404(User, username__iexact=user_name, is_active =True)
    def get_context_data(self, *args, **kwargs):
        context = super(ProfilesDetailView, self).get_context_data(*args, **kwargs)
        qs = RestaurantLocation.objects.filter(owner = self.get_object())
        if qs.exists:
            context['locations'] = qs
        return context


# Create your views here.

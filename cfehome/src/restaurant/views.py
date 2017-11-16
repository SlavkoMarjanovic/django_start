from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import RestaurantLocation
from .forms import RestorauntCreateForm, RestaurantLocationCreateForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RestaurantLocationSerializer

'''@login_required(login_url="/login/")
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit= False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect("/restaurant/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors

    template_name = 'restaurant/form.html'
    contex = {"form":form}
    return render(request, template_name, contex)





def restaurantlistview(request):
    template_name = "restaurant/restaurantlocation_list.html"
    query_set = RestaurantLocation.objects.all()
    contex ={
        "object_list" : query_set
    }
    return render(request, template_name, contex)
'''
class Restaurantlistview(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)
    def get_context_data(self, **kwargs):
        context = super(RestaurantDetailView, self).get_context_data(**kwargs)
        return context

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    success_url = '/restaurant/'

    def get_context_data(self, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(**kwargs)
        context['title']= 'Add restaurant'
        return context


    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurant/detail-update.html'
#    success_url = '/restaurant/'

    def get_context_data(self, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(**kwargs)
        name = self.get_object().name
        context['title'] = 'Update{}'.format(name)
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
class RestoranLocationList(APIView):
    def get(self, request):
        restaurant = RestaurantLocation.objects.all()
        serializer = RestaurantLocationSerializer(restaurant, many=True)
        return Response(serializer.data)
    def post(self):
        pass


            









#    return HttpResponse(html_)
# pozdrav
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import RestaurantLocation
from .forms import RestorauntCreateForm
from django.views.generic import TemplateView, ListView, DetailView


def restaurant_createview(request):
    form = RestorauntCreateForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            obj = RestaurantLocation.objects.create(
                name = form.cleaned_data.get("name"),
                location = form.cleaned_data.get("location"),
                category = form.cleaned_data.get("category")
            )
        return HttpResponseRedirect("/restaurant/")
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

class Restaurantlistview(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)

            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()
'''    def get_context_data(self, **kwargs):
        context = super(RestaurantDetailView, self).get_context_data(**kwargs)
        return context'''

            









#    return HttpResponse(html_)
# pozdrav
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import RestaurantLocation

#from django.views.generic import TemplateView
def restaurantlistview(request):
    template_name = "restaurant/restaurant_list.html"
    query_set = RestaurantLocation.objects.all()
    contex ={
        "object_list" : query_set
    }
    return render(request, template_name, contex)








#    return HttpResponse(html_)
# pozdrav
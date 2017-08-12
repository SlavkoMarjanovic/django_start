from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
'''

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        contex = super(HomeView, self).get_context_data(*args, **kwargs)
        num = random.randint(0, 1000000)
        some_list = [num, random.randint(0, 1000000), random.randint(0, 1000000)]
        contex = {
            "num": num,
            "some_list": some_list
        }

        print(contex)
        return contex

class AboutView(TemplateView):
    template_name = 'about.html'
class ContentView(View):
    def get(self, request, *args, **kwargs):
        contents = {}
        return render(request, "contact.html", contents)'''

#    return HttpResponse(html_)
# pozdrav
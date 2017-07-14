from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
# Function based view
'''def home(request):
    html_ = """ <!DOCTYPE html>
<html lang=en>

<head>
</head>
<body>
<h1>Hello word</h1>
<p>This is a {{html_var}} comming true</p>
</body>
</html>







    """
'''
def home(request):
    num = random.randint(0,1000000)
    some_list = [num, random.randint(0,1000000), random.randint(0,1000000)]
    contents = {
        "num":num,
        "bool_item":True,
        "some_list":some_list
    }
    return render(request, "home.html",contents)

def about(request):

    return render(request, "about.html")

def contact(request):

    return render(request, "contact.html")

#    return HttpResponse(html_)
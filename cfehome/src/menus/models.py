from django.db import models
from django.conf import settings
from restaurant.models import RestaurantLocation
from django.core.urlresolvers import reverse


class Item(models.Model):
    #assosiation
    user =      models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant =models.ForeignKey(RestaurantLocation)
    #real item staf
    name =      models.CharField(max_length=120)
    contents =  models.TextField(help_text= "Separate by comma")
    excludes = models.TextField(blank=True, null= True,help_text="Separate by comma")
    public =    models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ["-update","-timestamp"]
    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={"pk":self.pk})
    def get_contents(self):
        return self.contents.split(",")
    def get_excludes(self):
        return self.excludes.split(",")




# Create your models here.

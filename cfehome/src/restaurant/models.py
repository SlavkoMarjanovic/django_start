from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_category

# Create your models here.
User = settings.AUTH_USER_MODEL
class RestaurantLocation(models.Model):
    owner =          models.ForeignKey(User)
    name =          models.CharField(max_length=120)
    location =      models.CharField(max_length=120, null=True, blank=True)
    category =      models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp=      models.DateTimeField(auto_now_add=True)
    update =        models.DateTimeField(auto_now=True)
    slug =          models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('restaurant:detail', kwargs={"slug":self.slug})
    @property
    def title(self):
        return self.name
    #pozdrav
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender= RestaurantLocation)

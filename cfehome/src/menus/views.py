from django.shortcuts import render
from .models import Item
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user = self.request.user)

class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ItemForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['title']= 'Creating Item'
        return context
    def get_form_kwargs(self):
        kwargs = super(ItemCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = ItemForm
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        context['title']= 'Update view'
        return context

# Create your views here.
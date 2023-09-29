from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class VersionListView(ListView):
    model = Version

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     for data in context_data['object_list']:
    #         if data in Version.objects.all():
    #             context_data[]


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    form_class = ProductForm


class VersionUpdateView(UpdateView):
    model = Version
    success_url = reverse_lazy('catalog:home')
    form_class = VersionForm

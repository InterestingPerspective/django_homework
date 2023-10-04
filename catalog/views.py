from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductListView(ListView):
    model = Product


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = VersionForm(initial={'product': self.kwargs.get('pk')})
        return context_data


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('catalog:create_version')
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version_form'] = VersionForm(initial={'product': self.kwargs.get('pk')})
        return context_data


class VersionCreateView(CreateView):
    model = Version
    success_url = reverse_lazy('catalog:home')
    form_class = VersionForm

    def get_object(self, queryset=None):
        return self.request.version


class VersionUpdateView(UpdateView):
    model = Version
    success_url = reverse_lazy('catalog:home')
    form_class = VersionForm

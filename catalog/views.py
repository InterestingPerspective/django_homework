from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from catalog.services import get_cached_versions_for_product, get_category_list


class ProductListView(LoginRequiredMixin, ListView):
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['versions'] = get_cached_versions_for_product(self.object.pk)
        context_data['form'] = VersionForm(initial={'product': self.kwargs.get('pk')})
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:create_version')
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:home')
    form_class = ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version_form'] = VersionForm(initial={'product': self.kwargs.get('pk')})
        return context_data


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    success_url = reverse_lazy('catalog:home')
    form_class = VersionForm

    def get_object(self, queryset=None):
        return self.request.version


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    success_url = reverse_lazy('catalog:home')
    form_class = VersionForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_category_list()
        return context_data

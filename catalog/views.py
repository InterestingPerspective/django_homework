from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


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


def view_product(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    context = {
        'object': product_item
    }
    return render(request, 'catalog/product.html', context)

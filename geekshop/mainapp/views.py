from django.shortcuts import render
from .models import Product, ProductCategory, ProductManager
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger


MENU_LINKS = [
    {"href": "index", "active_if": ["index"], "name": "домой"},
    {
        "href": "products:index",
        "active_if": ["products:index", "products:category"],
        "name": "продукты",
    },
    {"href": "contact", "active_if": ["contact"], "name": "контакты"},
]


def index(request):
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp/index.html",
        context={
            "title": "Магазин",
            "content_block_class": "slider",
            "menu_links": MENU_LINKS,
            "products": products,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "content_block_class": "hero",
            "menu_links": MENU_LINKS,

        },
    )

def products_index(request):
    select_category_dict = {'name': 'Всё', 'href': reverse('products:index')}
    categories = [{'name': c.name, 'href': reverse('products:category', args=[c.id])} for c in
                  ProductCategory.objects.all()]
    categories = [{'name': 'Всё', 'href': reverse('products:index')}, *categories]
    products = Product.objects.order_by("price")

    page = request.GET.get('page', default='1')
    per_page = request.GET.get('per_page', default='4')
    paginator = Paginator(products, per_page)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(
        request,
        "mainapp/products_list.html",
        context={
            "title": "Каталог",
            "content_block_class": "hero-white",
            "menu_links": MENU_LINKS,
            "select_category": select_category_dict,
            "categories": categories,
            "hot_product": ProductManager.hot_product,
            "products": page,
        },
    )


def products(request, pk=None):
    select_category = get_object_or_404(ProductCategory, id=pk)
    select_category_dict = {
        'name': select_category.name,
        'href': reverse('products:category', args=[select_category.id])}

    categories = [{'name': c.name, 'href': reverse('products:category', args=[c.id])} for c in
                  ProductCategory.objects.all()]
    categories = [{'name': 'Всё', 'href': reverse('products:index')}, *categories]
    products = Product.objects.filter(category=select_category).order_by("price")
    return render(
        request,
        "mainapp/products_list.html",
        context={
            "title": "Каталог",
            "content_block_class": "hero-white",
            "menu_links": MENU_LINKS,
            "select_category": select_category_dict,
            "categories": categories,
            "products": products,

        },
    )

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Category, News, Author, Reference
from .forms import CategoryForm, NewsForm, AuthorForm, ReferenceForm
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    categories = services.get_categories_news_count()
    categories_count=services.get_categories_count()
    authors_count=services.get_categories_count()
    news_count=services.get_news_count()
    references_count=services.get_references_count()
    views=services.get_views()
    print(views)
    ctx = {
        "categories": categories,
        "categories_count":categories_count,
        "authors_count":authors_count,
        "news_count":news_count,
        "references_count":references_count,
        "views": views
    }
    return render(request, 'dashboard/index.html', ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


def category_list(request):
    categories = services.get_categories()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_edit(request, category_id):
    model = Category.objects.get(id=category_id)
    form = CategoryForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


def category_delete(request, category_id):
    model = Category.objects.get(id=category_id)
    model.delete()
    return redirect("category_list")


def news_list(request):

    news = services.get_news()
    ctx = {
        "news": news
    }
    return render(request, 'dashboard/news/list.html', ctx)


def news_create(request):
    model = News()
    form = NewsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def news_edit(request, news_id):
    model = News.objects.get(id=news_id)
    form = NewsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)


def delete_news(request, news_id):
    model = News.objects.get(id=news_id)
    model.delete()
    return redirect("news_list")


def authors_list(request):
    authors = services.get_authors()
    ctx = {
        "authors": authors
    }
    return render(request, 'dashboard/author/list.html', ctx)


def authors_create(request):
    model = Author()
    form = AuthorForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('authors_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/author/form.html', ctx)


def authors_edit(request, author_id):
    model = Author.objects.get(id=author_id)
    form = AuthorForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('authors_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/author/form.html', ctx)


def authors_delete(request, author_id):
    model = Author.objects.get(id=author_id)
    model.delete()
    return redirect("authors_list")


def references_list(request):

    references = services.get_references()
    ctx = {
        "references": references
    }
    return render(request, 'dashboard/reference/list.html', ctx)


def references_create(request):
    model = Reference()
    form = ReferenceForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('references_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/reference/form.html', ctx)


def references_edit(request, reference_id):
    model = Reference.objects.get(id=reference_id)
    form = ReferenceForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('references_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/reference/form.html', ctx)


def references_delete(request, reference_id):
    model = Author.objects.get(id=reference_id)
    model.delete()
    return redirect("references_list")

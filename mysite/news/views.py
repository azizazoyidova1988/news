from django.http import HttpResponse
from django.shortcuts import render, redirect
from dashboard.models import Category, Author, News, Reference
from django.utils import timezone
import datetime


def home(request):
    actuals = News.objects.all().filter(created_at__range=[timezone.now() - datetime.timedelta(days=1), timezone.now()])
    populars = News.objects.all().order_by("-views")[:4]
    fresh_news = News.objects.all().order_by("-created_at")[:4]
    politics = News.objects.all().filter(category_id=1)
    worlds = News.objects.all().filter(category_id=2)
    sports = News.objects.all().filter(category_id=4)
    sciences = News.objects.all().filter(category_id=3)
    abouts = News.objects.all().filter(category_id=6)
    news = News.objects.all()
    sums = News.objects.all().order_by("-views")
    categories = Category.objects.all()
    authors = Author.objects.all().order_by("-created_at")[:4]
    ctx = {
        "actuals": actuals,
        "populars": populars,
        "fresh_news": fresh_news,
        "politics": politics,
        "worlds": worlds,
        "sports": sports,
        "authors": authors,
        "sciences":sciences,
        "news": news,
        "sums": sums,
        "abouts": abouts,
        "categories": categories
    }
    return render(request, 'news/index.html', ctx)


def category(request, category_id):
    categories = Category.objects.all()
    news = News.objects.all().filter(category_id=category_id)
    fresh_news = News.objects.all().order_by("-created_at")[:4]
    new=news[0]
    new1=news[1:]
    ctx = {
        "new": new,
        "new1": new1,
        "fresh_news": fresh_news,
        "categories": categories
    }
    return render(request, 'news/category.html', ctx)



def view(request, news_id):
    categories = Category.objects.all()
    new = News.objects.all().get(id=news_id)
    new.views=new.views+1
    sums=News.objects.all().order_by("-views")
    authors = Author.objects.all().order_by("-created_at")[:2]
    fresh_news = News.objects.all().order_by("-created_at")[:4]

    ctx = {
        "categories": categories,
        "new": new,
        "sums":sums,
        "authors": authors,
        "fresh_news": fresh_news,
    }
    return render(request, 'news/view.html', ctx)



def contact(request):
    categories = Category.objects.all()
    reference = Reference()
    if request.POST:
        reference.name = request.POST.get("name")
        reference.email = request.POST.get("email")
        reference.message = request.POST.get("message")
        reference.save()
    ctx = {
        "categories": categories
    }
    return render(request, 'news/contact.html', ctx)

def search(request):
    # news=[]
    news = News.objects.all()
    categories = Category.objects.all()
    fresh_news = News.objects.all().order_by("-created_at")[:4]
    if request.GET and request.GET.get("search"):
        news = News.objects.filter(title__icontains=request.GET.get("search"))
        print("Search", news)
    ctx = {
        "news": news,
        "fresh_news": fresh_news,
        "search_count":len(news),
        "search_text":request.GET.get("search"),
        "categories": categories
    }
    return render(request, "news/search.html", ctx)


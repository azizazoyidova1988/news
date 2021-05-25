from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    full_name = models.TextField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=250,blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=500,blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True,on_delete=models.SET_NULL )
    author = models.ForeignKey(Author, blank=False, null=True, on_delete=models.SET_NULL)
    views = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Reference(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.CharField(max_length=250,blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

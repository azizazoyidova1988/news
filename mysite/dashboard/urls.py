from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category/list/', views.category_list, name="category_list"),
    path('category/add/', views.category_create, name="category_add"),
    path('category/<int:category_id>/edit/', views.category_edit, name="category_edit"),
    path('category/<int:category_id>/delete/', views.category_delete, name="category_delete"),

    path('news/list/', views.news_list, name="news_list"),
    path('news/add/', views.news_create, name="news_add"),
    path('news/<int:news_id>/edit/', views.news_edit, name="news_edit"),
    path('news/<int:news_id>/delete/', views.delete_news,name="delete_news"),

    path('authors/list/', views.authors_list, name="authors_list"),
    path('authors/add/', views.authors_create, name="authors_add"),
    path('authors/<int:author_id>/edit/', views.authors_edit, name="authors_edit"),
    path('authors/<int:author_id>/delete/', views.authors_delete, name="authors_delete"),

    path('references/list/', views.references_list, name="references_list"),
    path('references/add/', views.references_create, name="references_add"),
    path('references/<int:reference_id>/edit/', views.references_edit, name="references_edit"),
    path('references/<int:reference_id>/delete/', views.references_delete, name="references_delete"),

]

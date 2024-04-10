from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="/"),
    path("<int:page>", views.main, name="root_paginate"),
    path('author/<str:author>/', views.author_info, name='author_info'),
    path("new_author/", views.new_author, name="new_author"),
    path("new_quote/", views.new_quote, name="new_quote"),
    path("success/", views.success_url, name="success_url")
]

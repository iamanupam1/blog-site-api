from django import views
from django.urls import path

from .views import apiOverview, articleDetail, articleFeaturedList, articleList, commentAdd, contactInquiry, commentList, categoryList

urlpatterns = [
    path('',view=apiOverview,name='api-overview'),
    path('article-list/',view=articleList,name='article-list'),
    path('article-featured/',view=articleFeaturedList,name='article-featured'),
    path('article-detail/<str:pk>/',view=articleDetail, name='article-detail'),
    path('comments/add/',view=commentAdd,name='comment-add'),
    path('comments/<str:pk>/',view=commentList,name='comment-list'),
    path('category-list/',view=categoryList,name='comment-list'),
    path('contact-inquiry/',view=contactInquiry,name='contact-inquiry'),
]

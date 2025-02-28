from django.urls import path
from .views import news_view,load_more_articles 
urlpatterns = [
    path('', news_view, name= "news-view"),
    path("load-more/", load_more_articles, name="load_more"),
]

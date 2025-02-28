import requests
from requests.exceptions import HTTPError
from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse

def news_view(request):
    if request.method == "GET":
        country = request.GET.get('country', 'us')
        NEWS_API_KEY = settings.NEWS_API_KEY
        url = 'https://newsapi.org/v2/top-headlines'
        params = {
            'apiKey': NEWS_API_KEY,
            'country': country,
            'pageSize': 4,
            'page': 1
        }
        try:
            req = requests.get(url, params=params) # sending the urls and other parameters for response
            req.raise_for_status()
            result = req.json()
            articles = result.get("articles", [])
            # print(articles)
            context = {
                'page_obj': articles,
                'country': country
            }
            return render(request, 'news.html', context)
        except HTTPError as e:
            return render(request, 'news.html', {'error': f'HTTP Error: {e.response.status_code}'})
        except Exception as e:
            return render(request, 'news.html', {'error': str(e)})
    else:
        return render(request, 'news.html', {"country": "Failure for news"})

def load_more_articles(request):
    country = request.GET.get('country', 'us')
    NEWS_API_KEY = settings.NEWS_API_KEY
    NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
    page = int(request.GET.get("page", 1))
    country = request.GET.get("country", "us")

    response = requests.get(NEWS_API_URL, params={"country": country, "apiKey": NEWS_API_KEY, "page": page})
    data = response.json()

    articles = data.get("articles", [])
    return JsonResponse({"articles": articles})
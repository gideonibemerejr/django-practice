from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/index.html', {'title': 'Articles', 'articles': articles})

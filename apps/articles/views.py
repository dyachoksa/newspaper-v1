from django.views.generic import ListView, DetailView

from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    queryset = Article.published.order_by("-published_at").all()


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"

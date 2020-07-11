from django.views.generic import ListView, DetailView

from .models import Article, Category


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 10

    def get_queryset(self):
        category_slug = self.kwargs.get("slug")

        qs = Article.published.order_by("-published_at")

        if category_slug is not None:
            qs = qs.filter(category__slug=category_slug)

        return qs.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        category = None
        category_slug = self.kwargs.get("slug")

        if category_slug is not None:
            category = Category.objects.get(slug=category_slug)

        context.update({"category": category, "category_slug": category_slug})

        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"

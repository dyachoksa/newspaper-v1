from django.views.generic import TemplateView

from apps.articles.models import Article


class HomePageView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self):
        context = super().get_context_data()

        # main featured article
        featured_article = (
            Article.published.filter(is_featured=True).order_by("-published_at").first()
        )
        # additional featured articles
        extra_articles = Article.published.filter(is_featured=True).order_by(
            "-published_at"
        )[1:3]

        context.update(
            {"featured_article": featured_article, "extra_articles": extra_articles}
        )

        return context

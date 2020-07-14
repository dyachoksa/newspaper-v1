from django import template

from ..models import Article

register = template.Library()


@register.inclusion_tag("articles/tags/most_popular_articles.html")
def most_popular_articles():
    articles = Article.published.order_by("-comments_count").all()[:5]

    return {"articles": articles}


@register.inclusion_tag("articles/tags/category_featured_articles.html")
def category_featured_articles():
    articles = (
        Article.published.filter(is_category_featured=True)
        .order_by("-published_at")
        .all()[:5]
    )

    return {"articles": articles}

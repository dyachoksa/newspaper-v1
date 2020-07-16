from haystack import indexes

from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """Article search index model"""

    text = indexes.CharField(document=True, use_template=True)
    category = indexes.CharField(model_attr="category", null=True)
    published_at = indexes.DateTimeField(model_attr="published_at")

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().published.all()

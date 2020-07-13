from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from apps.comments.forms import CommentForm

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


class ArticleDetailView(SuccessMessageMixin, FormMixin, DetailView):
    model = Article
    context_object_name = "article"
    form_class = CommentForm
    success_message = "Thank you! Comment was successfully posted."

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        self.object = self.get_object()

        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        return self.form_invalid(form)

    def form_valid(self, form: CommentForm):
        comment = form.save(False)

        comment.user = self.request.user
        comment.article = self.object
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("articles:detail", args=(self.kwargs["pk"],))
